"""
The input models
"""

from typing import Dict, Optional, Literal, List, Union

from fastapi import Query
from pydantic import BaseModel


class IrisQuery(BaseModel):
    """
    <> below means optional
    The general query model:
    {
        <species: one or more of 'setosa', 'versicolor' or 'virginica' e.g. "setosa" or ["setosa", "virginica"]>
        <lower: the lower bound by column, default -- no bound, e.g. {"sepal_length": 5, "petal_length": 3}>
        <upper: the upper bound by column, default -- no bound, e.g. {"sepal_length": 5.2}>

    }
    """
    species: Optional[Union[str, List[Literal['setosa', 'versicolor', 'virginica']]]] = None
    lower: Optional[Dict[Literal['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], float]] = None
    upper: Optional[Dict[Literal['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], float]] = None
    page: int = Query(1, description='the page number', ge=1)
    per_page: int = Query(150, description='how many results per page', ge=1)
