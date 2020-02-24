from typing import Dict, Optional, Literal, List, Union

from pydantic import BaseModel


class IrisQuery(BaseModel):
    species: Optional[Union[str, List[Literal['setosa', 'versicolor', 'virginica']]]] = None
    lower: Optional[Dict[Literal['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], float]] = None
    upper: Optional[Dict[Literal['sepal_length', 'sepal_width', 'petal_length', 'petal_width'], float]] = None
