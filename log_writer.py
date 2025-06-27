from pymongo import MongoClient
import settings



db = settings.CLIENT[settings.MONGO_DB]

queries_db = db[settings.QUERY_DB]

queries_db.delete_many({})
    


def query_writer():
    queries = settings.QUERY_LOG
    result =queries_db.insert_many(queries)
    return 