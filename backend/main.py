from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.onedrive_file import CHUNK_SIZE
from langchain_text_splitters import RecursiveCharacterTextSplitter

file_path = "./caf.pdf"

loader = PyPDFLoader(file_path)
docs = loader.load()


# spit the content
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)
print(all_splits[1].page_content)
print("\n\n\n")
print(all_splits[2].page_content)
print("\n\n\n")
print(all_splits[3].page_content)
