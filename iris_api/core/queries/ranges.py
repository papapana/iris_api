"""
Core implementation of the endpoint /range/
"""

from typing import List, Dict, Any

from iris_api.app.api.models import IrisQuery
from iris_api.app.db import db
from iris_api.core.queries.utilities import create_range_query


def column_range(range_query: IrisQuery) -> List[Dict[str, Any]]:
    """
    :param range_query: An IrisQuery as defined in the models
    :return: a list of dictionaries with lower <= column <= upper
    """
    # do not show _id, show label
    projection = {'_id': 0, 'label': '$_id', 'sepal_length': 1, 'sepal_width': 1, 'petal_length': 1, 'petal_width': 1}
    query = create_range_query(range_query.species, range_query.lower, range_query.upper)
    db_cursor = db.features.find(query, projection)

    # take care of pagination
    if range_query.page is None and range_query.per_page is not None:
        db_cursor = db_cursor.limit(range_query.per_page)
    if range_query.page is not None and range_query.per_page is not None:
        db_cursor = db_cursor.skip(range_query.per_page * (range_query.page - 1)).limit(range_query.per_page)

    return list(db_cursor)
