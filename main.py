from fastapi import FastAPI
from pydantic import BaseModel, Field
all_students = {
        "Arvind" : 98,
        "Nikitha" : 100,
        "Ganja" : 32,
        "Purohit" : 21

    }

class Student(BaseModel):
    name : str = Field(..., min_length = 2, max_length = 50)
    marks : int = Field(..., ge = 1, le = 100)


app = FastAPI()

@app.get("/")
def root():
    return {"Message" : "SkillSphere Backend running"}

@app.get("/students")
def get_student_info(passed : bool = None):
   
    if passed is None:
        return {"Studetns": all_students}
    elif passed is True:
        return {"Students" :[nums for nums, marks in all_students.items() if marks > 60]}
    elif passed is False:
        return {"Students" :[nums for nums, marks in all_students.items() if marks < 60]}


@app.get("/skillsphere")
def get_app_info():
    return {"Message" : "SkillSphere 1.0"}


@app.get("/students/{student_name}")
def read_item(student_name : str):
    return {"student_name" : student_name}


@app.post("/students")
def post_data(student:Student):
    all_students[student.name] = student.marks
    return{
        "Message" : f"Student {student.name} added",
        "Current data " :  all_students
    }


