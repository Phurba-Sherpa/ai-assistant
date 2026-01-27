import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from supabase import Client, create_client

embed_model = "nomic-embed-text"


def load_env(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise RuntimeError(f"Environment variable {key} not set")
    return value


# Ensure .env content loaded to os env
load_dotenv(override=True)

# read for os env
sb_url: str = load_env("SUPABASE_URL")
sb_key: str = load_env("SUPABASE_KEY")
base_url = load_env("OLLAMA_BASE_URL")


supabase: Client = create_client(sb_url, sb_key)


embeddings = OllamaEmbeddings(model=embed_model, base_url=base_url)

vector_store = SupabaseVectorStore(
    embedding=embeddings,
    client=supabase,
    table_name="faqs",
    query_name="match_documents",
)

query = "What is the flow for card action?"
matched_docs = vector_store.similarity_search(query)
print(matched_docs[0].page_content)
