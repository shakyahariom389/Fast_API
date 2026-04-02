from sqlalchemy import text
from app.database import engine

def execute_query(sql):

    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = result.fetchall()

    return [dict(row._mapping) for row in rows]