import json 
from pathlib import Path


FILE_PATH = Path(__file__).parent / "student.json"
user = {
        "students" : []
    }
# check if JSON file exists if not create one 
try:
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        f.read()
        print("Success! we have a Json file ")
except FileNotFoundError:
    print("file does not exist create one !")
        # here i am trying to create a json file if it doesn't originally exist
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(user, f, indent=4)
        print(" we create one for you!")
#def student_info(user):
    #pass
# add a student information including name, age and department  
def add_student():
    name = input("> pls your name")
    age = input("> ")
    department = input("> ")
# this can be add to a CLI file later in the future

    student = {
        "name" : name,
        "age" : age,
        "department" : department    
        }
    user["students"].append(student)
    with open(FILE_PATH , "w", encoding="utf-8") as f:
        json.dump(user, f, indent=4)
        print(" saved to json! ")
        
# view students in the json file
def view_students():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f, indent=4)
        for studs in data["students"]:
            print(studs)
        
# search for student using their entry info ss
def search_(query): # this should hold a parameter of an input below 
    with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            for studs in data["students"]:
                if studs["name"] == query:
                    print(studs) #return the whole dictionary data in this (format name, matriculation_no and department)
                    return
            print(" Search not found ")
                    
# update a student
def update_(query): # this should hold a parameter of an input below 
    with open(FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                for studs in data["students"]:
                    if studs["name"] == query:
                        print(studs)
                        field = input(" what feild do you  want to update(age/department)")
                        studs[field] = input(">")
    with open(FILE_PATH, "r", encoding="utf-8") as f:
                data = json.dump(f, indent=4)
                
def delete_(query):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
    for i, student in enumerate(data["students"]):
        if student["name"].lower() == query.lower():
            removed = data["students"].pop(i)
            return "successfully removed"
    return None
# save all work to a .json file