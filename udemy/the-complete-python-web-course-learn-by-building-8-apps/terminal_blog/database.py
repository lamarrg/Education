import secure_data
import pymongo

class Database(object):
    URI = secure_data.database_uri  # This uri is an external mongodb that was set up on mlab.com. 
    DATABASE = None

    # is this method necessary if database is always live, as hosted by mlab.com?...
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['udemyblog']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

