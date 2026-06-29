from fastapi import FastAPI
# from fastapi import HTTPException
# from fastapi import status
# from schemas import StudentUpdate, StudentCreate, StudentResponse
# from database import all_students
from routers.students import router as student_router


# class Student(BaseModel):
#     name : str = Field(..., min_length = 2, max_length = 50)
#     marks : int = Field(..., ge = 1, le = 100)



app = FastAPI()
app.include_router(student_router)

@app.get("/")
def root():
    return {"Message" : "SkillSphere Backend running"}


@app.get("/skillsphere")
def get_app_info():
    return {"Message" : "SkillSphere 1.0"}


@app.get("/marks")
def get_marks(min_marks: int = 0):
    return {"minimum": min_marks}


