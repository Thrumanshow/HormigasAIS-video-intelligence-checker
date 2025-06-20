import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "XOXO Backend"
    port: int = 8000
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
