"""
DB provisioning script
"""
import os
import sys

import pandas as pd
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

url = 'https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv'

database_ = os.environ['MONGODB_DATABASE']
db_uri = 'mongodb://' + os.environ['MONGO_INITDB_ROOT_USERNAME'] + ':' + os.environ[
    'MONGO_INITDB_ROOT_PASSWORD'] + '@' + os.environ[
             'MONGODB_HOSTNAME'] + ':27017/'


def create_user():
    """
    Creates the appropriate user for the db
    :return:
    """
    print('Creating user ...')
    client = MongoClient(db_uri)
    try:
        client[database_].command("createUser", os.environ['MONGODB_USERNAME'], pwd=os.environ['MONGODB_PASSWORD'],
                                  roles=[{'role': 'readWrite', 'db': database_}])
    except OperationFailure:
        print('User already exists')
        return
    print('User created')


if __name__ == '__main__':
    df = pd.read_csv(url, index_col=False, header=0,
                     names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'label'])
    df.label = df.label.replace({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    client = MongoClient(db_uri)
    try:
        db_names = set(client.list_database_names())
        db = client['iris']
        if 'iris' in db_names and 'features' in db.list_collection_names():
            print('Database has already been provisioned')
            create_user()
            sys.exit(0)
        recs = df.to_dict(orient='records')
        print('Provisioning db...')
        db['features'].insert_many(recs)
        create_user()
        print('DB provisioned')
    except ServerSelectionTimeoutError as e:
        print('Timeout connecting to mongo, is mongo installed or uri correct? error: {}'.format(e))
        raise e
