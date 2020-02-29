"""
The input models
"""

from typing import Dict, Optional, Literal, List, Union

from fastapi import Query
from pydantic import BaseModel

IrisFlowersType = Literal['setosa', 'versicolor', 'virginica']
IrisColumnsType = Literal['sepal_length', 'sepal_width', 'petal_length', 'petal_width']


class IrisQuery(BaseModel):
    """
    <> below means optional
    The general query model:
    {
        <species: one or more of 'setosa', 'versicolor' or 'virginica' e.g. "setosa" or ["setosa", "virginica"]>
        <lower: the lower bound by column, default -- no bound, e.g. {"sepal_length": 5, "petal_length": 3}>
        <upper: the upper bound by column, default -- no bound, e.g. {"sepal_length": 5.2}>
        <page: the page number if pagination is used, int >=1 or not provided>
        <per_page: the results per page if pagination is used, int>=1 or not provided>
    }
    """
    species: Optional[Union[str, List[IrisFlowersType]]] = None
    lower: Optional[Dict[IrisColumnsType, float]] = None
    upper: Optional[Dict[IrisColumnsType, float]] = None
    page: Optional[int] = Query(default=None, description='the page number', ge=1)
    per_page: Optional[int] = Query(default=None, description='how many results per page', ge=1)
