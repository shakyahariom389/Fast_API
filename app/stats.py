from collections import Counter

# store queries
query_log = []

analytics_data = {
    "total_queries": 0,
    "common_keywords": [],
    "slowest_query": None
}

def update_stats(question, execution_time):

    query_log.append({
        "question": question,
        "time": execution_time
    })

    analytics_data["total_queries"] += 1

    # count keywords
    words = []
    for q in query_log:
        words.extend(q["question"].lower().split())

    counter = Counter(words)

    analytics_data["common_keywords"] = counter.most_common(5)

    # slowest query
    slowest = max(query_log, key=lambda x: x["time"])
    analytics_data["slowest_query"] = slowest