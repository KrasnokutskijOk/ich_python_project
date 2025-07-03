from pymongo import MongoClient
from datetime import datetime
import settings
import error_logger

def get_mongo_collection():
    try:
        client = settings.CLIENT
        db = client[settings.MONGO_DB]
        return db[settings.QUERY_DB]
    except Exception as e:
        error_logger.log_error(f"MongoDB connection error: {e}")
        raise


def write_log(search_type, params: dict, results_count: int):
    try:
        collection = get_mongo_collection()
        log = {
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "query_type": search_type,
            "params": params,
            "results_count": results_count
        }
        collection.insert_one(log)
    except Exception as e:
        error_logger.log_error(f"Error writing log to MongoDB: {e}")