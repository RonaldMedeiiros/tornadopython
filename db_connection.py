from decouple import config
from pymongo import MongoClient

MONGODB_URI = config("MONGODB_URI")
DATABASE_NAME = config("DATABASE_NAME")

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

transactions_collection = db['transactions']