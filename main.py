from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi import HTTPException
from fastapi import status



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
    if student_name not in all_students:
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "student name not found")
    else:
        marks = all_students[student_name]
        return {"student_name" : student_name,
                "marks" : marks}


@app.post("/students")
def post_data(student:Student):
    all_students[student.name] = student.marks
    return{
        "Message" : f"Student {student.name} added",
        "Current data " :  all_students
    }


@app.get("/marks")
def get_marks(min_marks: int = 0):
    return {"minimum": min_marks}

