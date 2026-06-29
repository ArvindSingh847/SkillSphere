from fastapi import APIRouter, HTTPException, status
from database import all_students
from schemas import StudentCreate, StudentUpdate, StudentResponse

router = APIRouter()

@router.get("/students")
def get_student_info(passed : bool = None):
   
    if passed is None:
        return {"Students": all_students}
    elif passed is True:
        return {"Students" :[student for student_id , student in all_students.items() if student["marks"] > 60]}
    elif passed is False:
        return {"Students" :[student for student_id, student in all_students.items() if student["marks"] < 60]}
    
    
@router.get("/students/{student_id}", response_model = StudentResponse)
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


@router.post("/students", response_model = StudentResponse)
def post_data(student:StudentCreate):
    new_id = max(all_students.keys()) + 1
    all_students[new_id] = {"id" :new_id,
                            "name" : student.name,
                            "email" : student.email,
                            "mobile_number" : student.mobile_number,
                            "career_goal" : student.career_goal,
                            "marks" : student.marks
    }
                            
    return all_students[new_id]
        

@router.put("/students/{student_id}", response_model = StudentResponse)
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



@router.delete("/students/{student_id}")
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
