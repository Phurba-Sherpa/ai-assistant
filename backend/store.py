import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import SupabaseVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from supabase import Client, create_client
from uuid import uuid4


embed_model = "nomic-embed-text"
file_path = "./caf.pdf"


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

loader = PyPDFLoader(file_path)
documents = loader.load()


# spit the content
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)

docs = text_splitter.split_documents(documents)
for doc in docs:
    doc.id = str(uuid4())

print(docs[0].id)

embeddings = OllamaEmbeddings(model=embed_model, base_url=base_url)

vector_store = SupabaseVectorStore.from_documents(
    docs,
    embeddings,
    client=supabase,
    table_name="faqs",
    query_name="match_documents",
)
