from fastapi import APIRouter

from ..controllers import evaluation_controller
from ..dtos.input import EvaluationInputDto

router = APIRouter(prefix="/evaluation")

@router.get("/")
async def get_evaluation(evaluation_input_dto: EvaluationInputDto) -> float:
    return evaluation_controller.get_evaluation(evaluation_input_dto.fen)
