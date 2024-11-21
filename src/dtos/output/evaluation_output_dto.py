from pydantic import BaseModel


class EvaluationOutputDto(BaseModel):
    evaluation: float
