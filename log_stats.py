import log_writer
import ui
import settings
import error_logger
from collections import Counter





def show_statistics() -> None:
    """
    Функция осущесвляет выборку 5 самых популярных и 5 последних запросов
    в базе данных MongoDB
    """
    try:
        collection = log_writer.get_mongo_collection()
    
        ui.print_recent_statistic_title()
        recent = list(collection.find().sort("timestamp", -1).limit(5))
        for item in recent:
            timestamp = item.get("timestamp", "—")
            query_type = item.get("query_type", "—")
            params = item.get("params", {})
            results_count = item.get("results_count", 0)
            ui.print_single_recent_log(timestamp, query_type, params, results_count)


        ui.print_top_5_statistic_title()
        most_common = list(collection.aggregate(settings.PIPELINE))
        for item in most_common:
            query_type = item.get("_id", "—")
            count = item.get("count", 0)
            ui.print_top_5_query_type(query_type, count)

    except Exception as e:
        error_logger.log_error(f"Error in show_statistics: {e}")
        ui.print_error("Failed to retrieve statistics.")