from fastapi import FastAPI, HTTPException
import pymongo
from bson.objectid import ObjectId
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
    try:
        insertResult = strat_collection.insert_one(strategy.model_dump())
        return {"document_id": str(insertResult.inserted_id)}
    except Exception as e:
        print("Error inserting strategy", e)
        raise HTTPException(status_code=400, detail="Error inserting strategy")


@app.get("/strategy/{strategy_id}")
def get_strategy(strategy_id: str):
    strategy_result = strat_collection.find_one({"_id": ObjectId(strategy_id)})
    if strategy_result:
        strategy_result["_id"] = str(strategy_result["_id"])
        return {"strat": strategy_result}
    else:
        raise HTTPException(status_code=404, detail="Strategy not found!")
