from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

tasks = [
    {"task": "learn fastapi", "completed": False},
    {"task": "build API", "completed": False}
]

class Task(BaseModel):
    task: str


@app.get("/")
def home():
    return {"Hello": "World"}


#creating a newtask
@app.post("/new_task")
def new_task(s: str):
    task = {
        "task": s,
        "completed": False
    }
    tasks.append(task)
    return {"tasks": tasks}

@app.get("/my_task")
def mytask():
    if not tasks:
        return {"message": "Empty Task"}
    return tasks

#update task done
@app.patch("/complete_task/{task_id}")
def complete_task(task_id: int):
    
    if task_id >= len(tasks):
        return {"error": "Task not found"}

    tasks[task_id]["completed"] = True
    return {"tasks": tasks}

#delete task
@app.delete("/delete_task/{task_id}")
def delete_task(task_id : int):
    if(task_id>= len(tasks)):
        return {"error" : "Task not found"}
    
    tasks.pop(task_id)
    return {"tasks": tasks}






