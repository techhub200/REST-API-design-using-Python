from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"task": "learn fastapi", "completed": False},
    {"task": "build API", "completed": False}
]

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

#get all the task
@app.get("/my_task")
def mytask():
    return tasks

#update task done
@app.put("/complete_task/{task_id}")
def complete_task(task_id : int):
    tasks[task_id]["completed"]=True
    return {"tasks" : tasks}
