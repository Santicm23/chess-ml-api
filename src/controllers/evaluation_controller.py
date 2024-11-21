import pandas as pd
from tensorflow import keras  # type: ignore

from ..config.logs import logger
from ..utils.fen import fen_to_one_hot_optimized


def get_evaluation(fen: str) -> float:
    logger.info(f"Received FEN: \033[1m{fen}\033[0m")

    one_hotted_fen = fen_to_one_hot_optimized(fen)

    logger.info(f"One-hotted FEN: \033[1m{pd.DataFrame([one_hotted_fen]).shape[1]} columns\033[0m")

    model = keras.models.load_model("./src/model/broken3.keras") # type: ignore

    logger.info(f"Model loaded: \033[1m{model}\033[0m")

    evaluation = model.predict(pd.DataFrame([one_hotted_fen]))[0][0] # type: ignore

    logger.info(f"Model prediction: \033[1m{evaluation}\033[0m")

    return evaluation # type: ignore
