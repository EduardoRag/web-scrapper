from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_user = os.getenv('MONGO_USER')
mongo_password = os.getenv('MONGO_PASS')

def get_database():
    connection_string = f"mongodb+srv://{mongo_user}:{mongo_password}@web-scraper.csutg7h.mongodb.net/"
    client = MongoClient(connection_string)

    return client['websites']