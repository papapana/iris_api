from typing import Optional, List, Union, Dict

from iris_api.app.db import db
from iris_api.core.queries.utilities import create_mean_query


def get_mean(species: Optional[Union[str, List[str]]] = None,
             lower: Optional[Dict[str, float]] = None,
             upper: Optional[Dict[str, float]] = None):
    print('here2')
    query = create_mean_query(species, lower, upper)

    return list(db.features.aggregate(query))
