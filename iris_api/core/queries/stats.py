"""
Code implementation for the endpoint /stats/mean
"""
from typing import Optional, List, Union, Dict

from iris_api.app.db import db
from iris_api.core.queries.utilities import create_mean_query


def get_mean(species: Optional[Union[str, List[str]]] = None,
             lower: Optional[Dict[str, float]] = None,
             upper: Optional[Dict[str, float]] = None,
             page: int = 1,
             per_page: int = 150
             ):
    """

    :param species: the species e.g. setosa
    :param lower: inclusive
    :param upper: not inclusive
    :param page: the result page
    :param per_page: how many results per page
    :return: the mean
    """
    query = create_mean_query(species, lower, upper)
    query.extend([{'$skip': per_page * (page - 1)}, {'$limit': per_page}])
    return list(db.features.aggregate(query))
