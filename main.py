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

class StudentCreate(BaseModel):
    name : str= Field(..., min_length = 2, max_length = 50)
    marks : int = Field(..., ge = 1, le = 100)
    # email : str = Field(..., min_length = 4, max_length = 30)
    # password : str = Field(..., min_length= 12, max_length= 8)

class StudentResponse(BaseModel):
    student_name : str= Field(..., min_length = 2, max_length = 50)
    marks : int = Field(..., ge = 1, le = 100)
    # email : str = Field(..., min_length = 4, max_length = 30)

class StudentUpdate(BaseModel):
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


@app.get("/students/{student_name}", response_model = StudentResponse)
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

@app.put("/students/{student_name}", response_model = StudentResponse)
def update_students(student_name : str, update : StudentUpdate):
    if student_name not in all_students:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "student not found"
        )
    
    
    all_students[student_name] = update.marks
    return {
        "student_name" : student_name,
        "marks" : all_students[student_name]
    }


@app.get("/marks")
def get_marks(min_marks: int = 0):
    return {"minimum": min_marks}


@app.delete("/students/{student_name}")
def delete_student(student_name : str):
    if student_name not in all_students:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "User does not exists"
        )
    del all_students[student_name]
    return {
        "message" : f"Deleted {student_name}'s account"
    }


