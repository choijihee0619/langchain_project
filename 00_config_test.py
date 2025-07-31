from dotenv import load_dotenv
import os

load_dotenv()
print(f"OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")
print(f"PINECONE_API_KEY: {os.getenv('PINECONE_API_KEY')}")