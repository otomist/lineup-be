from fastapi import FastAPI, HTTPException
import pymongo
from models import Strategy

app = FastAPI()

mongo_url = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongo_url)
db = client.lineup

strat_collection = db["strategies"]


@app.get("/")
def home():
    return "server is running"


@app.post("/strategy")
def add_strategy(strategy: Strategy):
    insertResult = strat_collection.insert_one(strategy.model_dump())
    return {"result": insertResult}


@app.get("/strategy/{strategy_id}")
def get_strategy(strategy_id: str):
    strategy = strat_collection.find_one({"id": strategy_id})
    if strategy:
        return strategy
    else:
        raise HTTPException(status_code=404, detail="Strategy not found!")
