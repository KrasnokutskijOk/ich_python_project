from pymongo import MongoClient
from datetime import datetime
import settings

def get_mongo_collection():
    client = settings.CLIENT
    db = client[settings.MONGO_DB]
    return db[settings.QUERY_DB]


def write_log(search_type, params: dict, results_count: int):
    collection = get_mongo_collection()
    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "query_type": search_type,
        "params": params,
        "results_count": results_count
    }
    collection.insert_one(log)