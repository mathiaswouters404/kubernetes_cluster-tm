from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/",
    "http://192.168.56.51:8000/users",
    "http://192.168.56.50/",
    "*"   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=[""],
)

client = MongoClient("mongodb://mongo:27017")
mydb=client["milestone2-mw"]
mycol=mydb["users"]

#test get hello world
@app.get("/")
async def root():
    return {"message : Hello World"}

@app.get("/users")
async def test():
    users = mycol.find()
    for user in users:
        item = user["name"]
    return {"name": item}