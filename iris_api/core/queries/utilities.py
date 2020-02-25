"""
Creation of the DB queries and other utilities
"""

from collections import defaultdict
from typing import List, Dict, Any, Optional, Union


def create_range_query(species: Union[str, List[str]], lower: Optional[Dict[str, float]],
                       upper: Optional[Dict[str, float]]) -> Dict[str, Any]:
    """
    Creates the appropriate mongodb query
    :param species:
    :param lower:
    :param upper:
    :return: mongodb query as a dictionary
    """
    query = defaultdict(dict)
    if lower:
        for col, val in lower.items():
            query[col]['$gte'] = val
    if upper:
        for col, val in upper.items():
            query[col]['$lte'] = val
    if isinstance(species, str):
        # noinspection PyTypeChecker
        query['label'] = species
    elif isinstance(species, list):
        query['label'] = {'$in': species}
    return dict(query)


def create_mean_query(species, lower, upper) -> List[Dict[str, Any]]:
    """
    Create the appropriate query for mean per column
    :param species:
    :param lower:
    :param upper:
    :return: mongodb query as a dictionary
    """
    query = []
    q = create_range_query(species, lower, upper)
    if q:
        query.append({'$match': q})
    query.append({'$group': {'_id': '$label', 'mean_sepal_length': {'$avg': '$sepal_length'},
                             'mean_sepal_width': {'$avg': '$sepal_width'},
                             'mean_petal_length': {'$avg': '$petal_length'},
                             'mean_petal_width': {'$avg': '$petal_width'}}})
    query.append({'$project': {'_id': 0, 'label': '$_id', 'mean_sepal_length': 1, 'mean_sepal_width': 1,
                               'mean_petal_length': 1, 'mean_petal_width': 1}})
    return query
