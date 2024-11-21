from pydantic import BaseModel


class EvaluationInputDto(BaseModel):
    fen: str
