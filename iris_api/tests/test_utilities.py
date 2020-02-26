"""
Testing the core.utilities package
"""
import pytest

from iris_api.core.queries.utilities import create_mean_query, create_range_query


def test_range_queries():
    """
    Tests scenarios for the utility create_range_query
    :return:
    """
    scenario1 = {}
    with pytest.raises(TypeError):
        create_range_query(**scenario1)

    scenario2 = {'species': None, 'lower': None, 'upper': None}
    q = create_range_query(**scenario2)
    assert q == {}, 'empty range should be returned'

    scenario3 = {'species': 'setosa', 'lower': None, 'upper': None}
    q = create_range_query(**scenario3)
    assert q == {'label': 'setosa'}, 'only setosa should be matched'

    scenario4 = {'species': ['setosa', 'versicolor'], 'lower': None, 'upper': None}
    q = create_range_query(**scenario4)
    assert q == {'label': {'$in': ['setosa', 'versicolor']}}, 'setosa and versicolor should be matched'

    scenario4 = {'species': ['setosa', 'versicolor'], 'lower': {'sepal_width': 4, 'sepal_length': 5},
                 'upper': {'sepal_length': 6}}
    q = create_range_query(**scenario4)
    expected = {'sepal_width': {'$gte': 4}, 'sepal_length': {'$gte': 5, '$lte': 6},
                'label': {'$in': ['setosa', 'versicolor']}}
    assert q == expected, 'setosa and versicolor should be matched with sepal_width >= 4, and 5 <= sepal_length <= 6'


def test_mean_queries():
    """
    Tests scenarios for the utility create_mean_query
    :return:
    """
    scenario1 = {}
    with pytest.raises(TypeError):
        create_mean_query(**scenario1)

    scenario2 = {'species': None, 'lower': None, 'upper': None, 'page': None, 'per_page': None}
    q = create_mean_query(**scenario2)
    expected = [{'$group': {'_id': '$label', 'mean_sepal_length': {'$avg': '$sepal_length'},
                            'mean_sepal_width': {'$avg': '$sepal_width'},
                            'mean_petal_length': {'$avg': '$petal_length'},
                            'mean_petal_width': {'$avg': '$petal_width'}}}, {
                    '$project': {'_id': 0, 'label': '$_id', 'mean_sepal_length': 1, 'mean_sepal_width': 1,
                                 'mean_petal_length': 1, 'mean_petal_width': 1}}]

    assert q == expected, 'the query should aggregate everything'

    scenario3 = {'species': ['virginica', 'setosa'], 'lower': None, 'upper': None, 'page': None, 'per_page': None}
    q = create_mean_query(**scenario3)
    expected = [{'$match': {'label': {'$in': ['virginica', 'setosa']}}}, {
        '$group': {'_id': '$label', 'mean_sepal_length': {'$avg': '$sepal_length'},
                   'mean_sepal_width': {'$avg': '$sepal_width'}, 'mean_petal_length': {'$avg': '$petal_length'},
                   'mean_petal_width': {'$avg': '$petal_width'}}}, {
                    '$project': {'_id': 0, 'label': '$_id', 'mean_sepal_length': 1, 'mean_sepal_width': 1,
                                 'mean_petal_length': 1, 'mean_petal_width': 1}}]
    assert q == expected, 'only the columns virginica and setosa must be included'

    scenario4 = {'species': ['setosa', 'versicolor'], 'lower': {'sepal_width': 3.0}, 'upper': {'sepal_length': 6.1},
                 'page': None, 'per_page': None}
    q = create_mean_query(**scenario4)
    expected = [{'$match': {'sepal_width': {'$gte': 3.0}, 'sepal_length': {'$lte': 6.1},
                            'label': {'$in': ['setosa', 'versicolor']}}}, {
                    '$group': {'_id': '$label', 'mean_sepal_length': {'$avg': '$sepal_length'},
                               'mean_sepal_width': {'$avg': '$sepal_width'},
                               'mean_petal_length': {'$avg': '$petal_length'},
                               'mean_petal_width': {'$avg': '$petal_width'}}}, {
                    '$project': {'_id': 0, 'label': '$_id', 'mean_sepal_length': 1, 'mean_sepal_width': 1,
                                 'mean_petal_length': 1, 'mean_petal_width': 1}}]
    assert q == expected, 'only setosa and versicolor should be included and for both sepal_width >= 3.0 and ' \
                          'sepal_length <= 6.1'
