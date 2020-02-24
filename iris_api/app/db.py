"""
Create connection to the MongoDB database
"""

from pymongo import MongoClient

client = MongoClient()

if 'iris' not in client.list_database_names():
    raise ConnectionError('Could not find the iris database')

db = client['iris']

if 'features' not in db.list_collection_names():
    raise ConnectionError('The database has not been populated')
