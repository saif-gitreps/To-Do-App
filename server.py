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
    
    if len(dataMap)+1 in dataMap:
        dataMap[len(dataMap)+2]=  {"task": task,"date":currentDate}    
    else: 
        dataMap[len(dataMap)+1]=  {"task": task,"date":currentDate}
    
    with open(dataFile,"w") as file:
        json.dump(dataMap,file)
    return {"message":"task added succesfully"}

@app.put("/task/update")
def update_task(task_id: str, updateTask : Task):
    with open(dataFile,"r") as file:
        dataMap = json.load(file)
    if task_id not in dataMap or task_id < 0:
        return {"message" : "no such task exists"}
    dataMap[task_id]["task"] = updateTask.task
    with open(dataFile, "w") as file:
        json.dump(dataMap,file)
    return {"message":"task updated successfully"} 

     


    
    
