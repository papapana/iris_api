"""
REST API implementation of the endpoint /range/
"""
from fastapi import APIRouter

from iris_api.app.api.models import IrisQuery
from iris_api.core.queries.ranges import column_range

router = APIRouter()


@router.post("/range/")
async def ranges(range_query: IrisQuery):
    """
     REST API endpoint /range/
    :param range_query:
    :return: json result for the specified range
    """
    return column_range(**range_query.dict())
