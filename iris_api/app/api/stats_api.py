from fastapi import APIRouter

from iris_api.app.api.models import IrisQuery
from iris_api.core.queries.stats import get_mean

router = APIRouter()


@router.post("/stats/mean/")
async def get_stats_mean(range_query: IrisQuery):
    return get_mean(**range_query.dict())
