"""
Core implementation of the endpoint /range/
"""

from typing import Optional, List, Dict, Union, Any

from iris_api.app.db import db
from iris_api.core.queries.utilities import create_range_query


def column_range(species: Optional[Union[str, List[str]]] = None,
                 lower: Optional[Dict[str, float]] = None,
                 upper: Optional[Dict[str, float]] = None) -> List[Dict[str, Any]]:
    """

    :param species: the species e.g. setosa
    :param lower: inclusive
    :param upper: not inclusive
    :return: a list of dictionaries with lower <= column <= upper
    """
    projection = {'_id': 0, 'label': '$_id', 'sepal_length': 1, 'sepal_width': 1, 'petal_length': 1, 'petal_width': 1}
    query = create_range_query(species, lower, upper)
    return list(db.features.find(query, projection))
