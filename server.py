from fastapi import FastAPI, Path
import json

app = FastAPI()
dataFile = "database.json"

@app.get("/tasks")
def see_tasks():
    