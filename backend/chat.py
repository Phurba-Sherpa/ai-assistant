import os

from dotenv import load_dotenv
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_ollama import ChatOllama, OllamaEmbeddings
from storage3 import create_client
from supabase import Client, create_client

# llm config
chat_model = "llama3.1:latest"
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

"""
For RAG application, we need 3 components
1. Chat model
2. Embed model
3. Vector store
"""
llm = ChatOllama(model=chat_model, base_url=base_url)
embeddings = OllamaEmbeddings(model=embed_model, base_url=base_url)
supabase: Client = create_client(sb_url, sb_key)
vector_store = SupabaseVectorStore(
    embedding=embeddings,
    client=supabase,
    table_name="faqs",
    query_name="match_documents",
)


messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]
resp = llm.invoke(messages)
