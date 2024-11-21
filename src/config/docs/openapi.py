from fastapi import FastAPI

__project__ = "chess-ml-api"


def load_metadata(app: FastAPI) -> None:
    app.title = __project__
    app.description = __project__
    app.version = "0.1.0"
