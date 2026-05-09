tasks_not_done = ["Do work"]
tasks_in_progress = []
tasks_done = []

tasks = {"Not Done": tasks_not_done,
         "In Progress": tasks_in_progress,
         "Done": tasks_done}

def Add():
    new_task = input("Please add a task: ")
    tasks["Not Done"].append(new_task)
    print("New task is added")
    for key, value in tasks.items():
        print(f"{key}: {value}")

def Update():
    current_task = input("Where is the task located (Not Done / In Progress / Done): ")
    which_task = input(f"Which task would you like to move:\n {tasks[current_task]}\n Please enter a task: ")
    location_task = input("Where would you like to move the task (Not done / In Progress / Done); ")
    tasks[current_task].remove(which_task)
    tasks[location_task].append(which_task)
    print("Task has been updated:")
    for key, value in tasks.items():
        print(f"{key}: {value}")

def Delete():
    task_deletee = input("Where is the task located (Not Done / In Progress / Done): ")
    which_task = input(f"Which task would you like to delete:\n {tasks[task_deletee]}\n Please enter a task: ")
    tasks[task_deletee].remove(which_task)
    print("Task deleted")
    for key, value in tasks.items():
        print(f"{key}: {value}")


print("Welcome to your Task Tracker")

while True:
    action = input("What would you like to do (Add / Update / Delete): ")
    if action.lower() == "add":
        Add()
    elif action.lower() == "update":
        Update()
    elif action.lower() == "delete":
        Delete()
    
    continue_using = input("Would you like to continue using the Task Tracker (Y/N): ")
    if continue_using.lower() == "y":
        print("Okay enjoy!")
    else:
        print("Okay Goodbye!")
        break
