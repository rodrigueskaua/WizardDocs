from pydantic import BaseSettings

class Settings(BaseSettings):
    app_port: int = 8000
    chromadb_dir: str = "/data/chromadb"

    class Config:
        env_file = ".env"

settings = Settings()