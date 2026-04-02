from app.nlp_to_sql import generate_sql

def test_python_query():
    q = "How many students enrolled in Python courses in 2024?"
    sql = generate_sql(q)
    assert "python" in sql.lower()