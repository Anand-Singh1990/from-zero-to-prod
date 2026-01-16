from fastapi import APIRouter, HTTPException
from app.models.schemas.requests import NumbersRequest
from app.workflows.sample_flow import stats_flow

router = APIRouter()

@router.get("/health")
def health():
    try:
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/stats")
def calculate_statistics(payload: NumbersRequest):
    try:
        result = stats_flow(payload.numbers)
        return {
            "status": "success",
            "data": result,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
