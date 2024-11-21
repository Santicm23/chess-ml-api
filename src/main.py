import uvicorn

from .config.docs import load_metadata
from .config.environment.read_env import DEV, PORT
from .server import app


def main(dev: bool = False) -> None:
    load_metadata(app)

    uvicorn.run(f"{__package__}.main:app", reload=dev, port=PORT)


if __name__ == "__main__":
    main(DEV)
