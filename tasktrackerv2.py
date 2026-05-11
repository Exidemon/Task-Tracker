import argparse

tasks = {
    
}

parser = argparse.ArgumentParser(description='Test')
parser.add_argument('-a','--add', type=str, help='Adds a task')
args = parser.parse_args()

print(args.add)

def Add(task):
    