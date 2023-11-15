from fastapi import FastAPI
from datetime import datetime as dt
from pydantic import BaseModel
import json

app = FastAPI()
dataFile = "database.json"

class Task(BaseModel):
    task : str
    date : str

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
    
    dataMap["counter(unrelated)"] += 1
    dataMap[dataMap["counter(unrelated)"]]=  {"task": task,"date":currentDate}    
    
    with open(dataFile,"w") as file:
        json.dump(dataMap,file)
    return {"message":"task added succesfully"}

@app.put("/task/update/{task_id}")
def update_task(task_id: str, updateTask : Task):
    with open(dataFile,"r") as file:
        dataMap = json.load(file)
        
    if task_id not in dataMap or int(task_id) < 0:
        return {"message" : "no such task"}
    dataMap[task_id] = updateTask.dict()
    
    with open(dataFile, "w") as file:
        json.dump(dataMap,file)
    return {"message":"task updated successfully"}

class PatchTask(BaseModel):
    task : str = None
    date: str = None

@app.patch("/task/patch/{task_id}")
def patch_task(task_id: str, task: PatchTask):
    with open(dataFile, "r") as file:
        dataMap = json.load(file)
    
    if task_id not in dataMap:
        return {"message" : "no such tasks"}
    
    if task.task != None:
        dataMap[task_id]["task"] = task.task
    if task.date != None:
        dataMap[task_id]["date"] = task.date
    
    with open(dataFile, "w") as file:
        json.dump(dataMap,file)
    return {"message" : "task patched successfully"}

@app.delete("/task/delete/{task_id}")
def delete_task(task_id: str):
    with open(dataFile,"r") as file:
        dataMap = json.load(file)
    
    if task_id not in dataMap:
        return {"message": "no such tasks"}
    del dataMap[task_id]
    
    with open(dataFile, "w") as file:
        json.dump(dataMap, file)
    return {"message" : "task deleted successfully"}





     


    
    
