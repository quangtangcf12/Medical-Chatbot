from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

extracted_data = load_pdf_file(data ='data/')
filter_data = filter_to_minimal_docs(extracted_data)
text_chunk = text_split(filter_data)

embedding = download_embeddings()

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)


index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    
index = pc.Index(index_name)

BATCH_SIZE = 50

for i in range(0, len(text_chunk), BATCH_SIZE):
    batch = text_chunk[i:i + BATCH_SIZE]
    PineconeVectorStore.from_documents(
        documents=batch,
        embedding=embedding,
        index_name=index_name
    )