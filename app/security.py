def is_safe_query(sql):

    sql = sql.lower()

    forbidden = ["delete","drop","update","insert"]

    for word in forbidden:

        if word in sql:
            return False

    return sql.strip().startswith("select")