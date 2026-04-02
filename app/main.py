from fastapi import FastAPI
from contextlib import asynccontextmanager
import time

from app.database import get_db, engine
from app.executor import execute_query
from app.models import Base
from app.schemas import QueryRequest
from app.nlp_to_sql import generate_sql
from app.stats import update_stats, analytics_data
# Create tables
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up FastAPI app...")
    yield
    print("Shutting down FastAPI app...")

app = FastAPI(lifespan=lifespan)

# Root
@app.get("/")
def read_root():
    return {"message": "FastAPI app is running!"}



@app.post("/query")
def query(req: QueryRequest):
    start = time.time()

    sql = generate_sql(req.question)
    result = execute_query(sql)

    execution_time = time.time() - start

    update_stats(req.question, execution_time)

    return {
        "sql": sql,
        "result": result,
        "execution_time": execution_time
    }



@app.get("/stats")
def stats():
    return analytics_data


# Run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)