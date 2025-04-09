import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
  def __init__(self):
    self.app_port = int(os.getenv("APP_PORT", 8000))
    self.chromadb_dir = os.getenv("CHROMADB_DIR", "/data/chromadb")
    self.openai_api_key = os.getenv("OPENAI_API_KEY", "")

settings = Settings()