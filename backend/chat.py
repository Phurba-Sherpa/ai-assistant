import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_openai import ChatOpenAI
from storage3 import create_client
from supabase import Client, create_client

# llm config
chat_model = "gpt-oss:20b-cloud"
# chat_model = "google/gemini-2.5-flash"
embed_model = "nomic-embed-text"


# Load .env content into os env
load_dotenv()


# helper func to extract env var
def load_env(key: str):
    value = os.getenv(key)

    if value is None:
        raise RuntimeError(f"Environment key {key} not set.")
    return value


# extract key
ls_tracing = load_env("LANGSMITH_TRACING")
ls_key = load_env("LANGSMITH_API_KEY")
base_url = load_env("OLLAMA_BASE_URL")
sb_url: str = load_env("SUPABASE_URL")
sb_key: str = load_env("SUPABASE_KEY")
# or_base_url = load_env("OPENROUTER_BASE_URL")
# or_key = load_env("OPENROUTER_API_KEY")

"""
For RAG application, we need 3 components
1. Chat model
2. Embed model
3. Vector store
"""
llm = ChatOllama(model=chat_model, base_url=base_url)
# llm = ChatOpenAI(
#     model=chat_model, api_key=or_key, base_url=or_base_url, max_tokens=15000
# )
embeddings = OllamaEmbeddings(model=embed_model, base_url=base_url)
supabase: Client = create_client(sb_url, sb_key)
vector_store = SupabaseVectorStore(
    embedding=embeddings,
    client=supabase,
    table_name="faqs",
    query_name="match_documents",
)


# Tool definition
@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to help answer a query"""
    retrieved_docs = vector_store.similarity_search(query, k=5)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs


tools = [retrieve_context]
# query = "What is the new card activation flow? Explain in layman language"
query = "नयाँ कार्ड सक्रिय गर्ने प्रक्रिया के हो? साधारण भाषामा व्याख्या गर्नुहोस्।"
prompt = (
    "You have access to a tool that retrieves context from a blog post. "
    "Use the tool to help answer user queries."
)
agent = create_agent(llm, tools, system_prompt=prompt)
for event in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    event["messages"][-1].pretty_print()
