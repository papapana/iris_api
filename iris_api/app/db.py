"""
Create connection to the MongoDB database
"""

import os 
db_uri = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
client = MongoClient(db_uri)

if 'iris' not in client.list_database_names():
    raise ConnectionError('Could not find the iris database')

db = client['iris']

if 'features' not in db.list_collection_names():
    raise ConnectionError('The database has not been populated')
