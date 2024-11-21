from fastapi import APIRouter

from ..controllers import evaluation_controller
from ..dtos.input import EvaluationInputDto
from ..dtos.output import EvaluationOutputDto

router = APIRouter(prefix="/evaluation", tags=["evaluation"])


@router.post("/")
async def get_evaluation(
    evaluation_input_dto: EvaluationInputDto,
) -> EvaluationOutputDto:
    return EvaluationOutputDto(
        evaluation=evaluation_controller.get_evaluation(evaluation_input_dto.fen)
    )
