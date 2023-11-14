from fastapi import FastAPI, Path , Body
from datetime import datetime as dt
from pydantic import BaseModel
import json

app = FastAPI()
dataFile = "database.json"

class Task(BaseModel):
    taskId: int
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
        dataArr = json.load(file)
    
    currentDate = dt.now().strftime("%d-%m-%Y") 
    dataArr.append({"task id": len(dataArr)+1,"task": task,"date":currentDate})
    
    with open(dataFile,"w") as file:
        json.dump(dataArr,file)
    return {"message":"task added succesfully"}



    
    
