import main
import log_writer
import ui
import settings 
from pymongo import MongoClient
from datetime import datetime
from collections import Counter





def show_statistics():
    collection = log_writer.get_mongo_collection()
    
    ui.print_recent_statistic_title()
    recent = list(collection.find().sort("timestamp", -1).limit(5))
    for item in recent:
        timestamp = item.get("timestamp", "—")
        query_type = item.get("query_type", "—")
        params = item.get("params", {})
        results_count = item.get("results_count", 0)
        ui.print_single_recent_log(timestamp, query_type, params, results_count)


    top_5_statistic = ui.print_top_5_statistic_title()
    most_common = list(collection.aggregate(settings.PIPELINE))
    for item in most_common:
        query_type = item.get("_id", "—")
        count = item.get("count", 0)
        ui.print_top_5_query_type(query_type, count)