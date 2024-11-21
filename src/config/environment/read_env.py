import os

from dotenv import load_dotenv

load_dotenv()


def read_env(key: str, default: str | None = None) -> str:
    value = os.getenv(key)
    if value is None:
        if default is None:
            raise ValueError(f"Environment variable {key} is required")
        return default
    return value


DEV = read_env("ENVIRONMENT", "dev") == "dev"
PORT = int(read_env("PORT", "8000"))
WEB_URL = read_env("WEB_URL", "http://localhost:5173")
