"""
Code implementation for the endpoint /stats/mean
"""

from iris_api.app.api.models import IrisQuery
from iris_api.app.db import db
from iris_api.core.queries.utilities import create_mean_query


def get_mean(range_query: IrisQuery):
    """
    :param range_query: An IrisQuery as defined in the models
    :return: the mean for all the columns for the selected species respecting constraints
    """
    query = create_mean_query(range_query.species, range_query.lower, range_query.upper, range_query.page,
                              range_query.per_page)
    return list(db.features.aggregate(query))
