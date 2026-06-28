from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi import HTTPException
from fastapi import status



all_students = {
        1 : {
            "name" : "Arvind",
            "email" : "arvind@gmail.com",
            "mobile_number" : "9492581304",
            "career_goal": "AI Engineer",
            "marks" : 98
        },

        2 : {
            "name" : "Nikitha",
            "email" : "nikitha@gmail.com",
            "mobile_number" : "7993502093",
            "career_goal" : "Data Scientist",
            "marks" : 100
        },

        3 : {
            "name" : "Tarun",
            "email" : "tarun@gmail.com",
            "mobile_number" : "MLOps Engineer",
            "marks" : 100
        },

        4 : {
            "name" : "Aditya",
            "email" : "aditya@gmail.com",
            "mobile_number" : "9398879682",
            "career_goal" : "Software Engineer",
            "marks" : 95
        },

        5 : {
            "name" : "Rickey",
            "email" : "rickey@gmail.com",
            "mobile_number" : "6300656893",
            "career_goal" : "Data Engineer",
            "marks" : 94
        }

    }

# class Student(BaseModel):
#     name : str = Field(..., min_length = 2, max_length = 50)
#     marks : int = Field(..., ge = 1, le = 100)

class StudentCreate(BaseModel):

    name : str= Field(..., min_length = 2, max_length = 50)
    email : str = Field(..., min_length = 4, max_length = 30)
    mobile_number : str = Field(..., min_length = 10, max_length = 10)
    career_goal : str = Field(..., min_length = 6, max_length = 15)
    marks : int = Field(..., ge = 1, le = 100)


class StudentResponse(BaseModel):
    id :int = Field(..., ge = 1, le= 100)
    name : str= Field(..., min_length = 2, max_length = 50)
    email : str = Field(..., min_length = 4, max_length = 30)
    mobile_number : str = Field(..., min_length = 10, max_length = 10)
    career_goal : str = Field(..., min_length = 6, max_length = 15)
    marks : int = Field(..., ge = 1, le = 100)


class StudentUpdate(BaseModel):
    name : str= Field(..., min_length = 2, max_length = 50)
    email : str = Field(..., min_length = 4, max_length = 30)
    mobile_number : str = Field(..., min_length = 10, max_length = 10)
    career_goal : str = Field(..., min_length = 6, max_length = 15)
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
        return {"Students" :[student for student_id , student in all_students.items() if student["marks"] > 60]}
    elif passed is False:
        return {"Students" :[student for student_id, student in all_students.items() if student["marks"] < 60]}


@app.get("/skillsphere")
def get_app_info():
    return {"Message" : "SkillSphere 1.0"}


@app.get("/students/{student_id}", response_model = StudentResponse)
def read_item(student_id : int):
    if student_id not in all_students:
       raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = "student name not found")
    else:
        student = all_students[student_id]
        return {
            'id' : student_id, 
            "name" :student["name"], 
            "email" :student["email"] ,
            "mobile_number": student["mobile_number"], 
            "career_goal" : student["career_goal"],
            "marks" : student["marks"]
        }


@app.post("/students", response_model = StudentResponse)
def post_data(student:StudentCreate):
    new_id = max(all_students.keys()) + 1
    all_students[new_id] = {"id" :new_id,
                            "name" : student.nameumber,
                            "email" : student.email,
                            "mobile_number" : student.mobile_number,
                            "career_goal" : student.career_goal,
                            "marks" : student.marks
    }
                            
    return all_students[new_id]
    

@app.put("/students/{student_id}", response_model = StudentResponse)
def update_students(student_id : int, update : StudentUpdate):
    if student_id not in all_students:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "student not found"
        )
    
    
    all_students[student_id] = {"id" :student_id,
                            "name" : update.name,
                            "email" : update.email,
                            "mobile_number" : update.mobile_number,
                            "career_goal" : update.career_goal,
                            "marks" : update.marks
    }
    return all_students[student_id]


@app.get("/marks")
def get_marks(min_marks: int = 0):
    return {"minimum": min_marks}


@app.delete("/students/{student_id}")
def delete_student(student_id : int):
    if student_id not in all_students:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Student does not exists"
        )
    del all_students[student_id]
    return {
    "message": f"Student {student_id} deleted successfully"
}


