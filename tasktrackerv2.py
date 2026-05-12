import argparse
import json

tasks = {}
parser = argparse.ArgumentParser(description='Test')
parser.add_argument('-a','--add', type=str, help='Adds a task', nargs='+')
parser.add_argument('-u','--update', type=str, help='Updates a task', nargs='+')
parser.add_argument('-d','--delete', type=str, help='Deletes a task', nargs='+')
args = parser.parse_args()

print(args.add)

def Add():
    tasks_id = 1
    details = args.add
    tasks[tasks_id] = {
        'status' : details[0],
        "description": details[1],
        'created_at' : details[2]
    }
    with open("tasks.json", "w") as outfile:
        json.dump(tasks, outfile)  
    tasks_id += 1

if args.add:
    Add()
else:
    None

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