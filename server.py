from fastapi import FastAPI, Path , Body
from datetime import datetime as dt
from pydantic import BaseModel
import json

app = FastAPI()
dataFile = "database.json"

class Task(BaseModel):
    task : str

@app.get("/tasks")
def see_tasks():
    with open(dataFile, "r") as file:
        data = json.load(file)
    return data

@app.post("/tasks/new-task")
def add_new_task(task: str):
    with open(dataFile,"r") as file:
        dataMap = json.load(file)
    
    currentDate = dt.now().strftime("%d-%m-%Y")
    
    dataMap["counter"] += 1
    dataMap[dataMap["counter"]]=  {"task": task,"date":currentDate}    
    
    with open(dataFile,"w") as file:
        json.dump(dataMap,file)
    return {"message":"task added succesfully"}

@app.put("/task/update")
def update_task(task_id: str, updateTask : Task):
    with open(dataFile,"r") as file:
        dataMap = json.load(file)
    if task_id not in dataMap or task_id < 0:
        return {"message" : "no such task"}
    dataMap[task_id]["task"] = updateTask.task
    with open(dataFile, "w") as file:
        json.dump(dataMap,file)
    return {"message":"task updated successfully"}

@app.delete("/task/delete")
def delete_task(task_id: str):
    with open(dataFile,"r") as file:
        dataMap = json.load(file)
    if task_id not in dataMap:
        return {"message": "no such tasks"}
    del dataMap[task_id]
    with open(dataFile, "w") as file:
        json.dump(dataMap, file)
    return {"message" : "task deleted successfully"}





     


    
    
