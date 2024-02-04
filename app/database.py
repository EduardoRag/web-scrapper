from pymongo import MongoClient

def get_database():
    connection_string = "mongodb+srv://eduardo:Ace2707093096@web-scraper.csutg7h.mongodb.net/"
    client = MongoClient(connection_string)

    return client['websites']