import argparse
import json


parser = argparse.ArgumentParser(description='Test')
parser.add_argument('-a','--add', type=str, help='Adds a task', nargs= 3)
parser.add_argument('-u','--update', type=str, help='Updates a task', nargs= 2)
parser.add_argument('-d','--delete', type=str, help='Deletes a task', nargs= 1)
args = parser.parse_args()

try:
    with open("tasks.json", "r") as infile:
            tasks = json.load(infile) 
except:
    tasks = { 0: {
                'status' : {},
                "description": {},
                'created_at': {} 
    }
             
            }

if tasks:
    tasks_id = max(int(i) for i in tasks.keys()) + 1
else:
    tasks_id = 1

def Add():
    global tasks_id
    details = args.add
    tasks[tasks_id] = {
        'status' : details[0],
        "description": details[1],
        'created_at' : details[2]
    }
    with open("tasks.json", "w") as outfile:
        json.dump(tasks, outfile)  

    tasks_id += 1
    

def Update():
    global tasks_id
    details = args.update
    task_id = details[0]
    tasks[task_id]["description"] = details[1]
    with open("tasks.json", "w") as outfile:
        json.dump(tasks, outfile)

def Delete():
    None

if args.add:
    Add()
elif args.update:
    Update()
elif args.delete:
    Delete()

# tasks = {}

# task_id = 1

# while True:
#     name = input("Enter task name: ")

#     if name == "quit":
#         break

#     tasks[task_id] = {
#         "name": name,
#         "completed": False
#     }

#     task_id += 1

# print(tasks)