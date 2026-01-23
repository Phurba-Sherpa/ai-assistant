import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

embed_model = "nomic-embed-text"
file_path = "./caf.pdf"

# Ensure .env content loaded to os env
load_dotenv(override=True)

# read for os env
base_url = os.getenv("OLLAMA_BASE_URL")

loader = PyPDFLoader(file_path)
docs = loader.load()


# spit the content
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)


embeddings = OllamaEmbeddings(model=embed_model, base_url=base_url)
vector_1 = embeddings.embed_query(all_splits[0].page_content)

print(f"Generated vectors of length {len(vector_1)}\n")
print(vector_1[:10])
