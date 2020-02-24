"""
DB provisioning script
"""

import sys

import pandas as pd
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

url = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'

if __name__ == '__main__':
    df = pd.read_csv(url, index_col=False, header=0,
                     names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'label'])
    df.label = df.label.replace({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    client = MongoClient()
    try:
        db_names = set(client.list_database_names())
        db = client['iris']
        if 'iris' in db_names and 'features' in db.list_collection_names():
            print('Database has already been provisioned')
            sys.exit(0)
        recs = df.to_dict(orient='records')
        db['features'].insert_many(recs)
    except ServerSelectionTimeoutError as e:
        print('Timeout connecting to mongo, is mongo installed or uri correct? error: {}'.format(e))
        raise e
