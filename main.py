from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Message" : "SkillSphere Backend running"}

@app.get("/students")
def get_student_info(passed : bool = None):
    all_students = {
        "Arvind" : 98,
        "Nikitha" : 100,
        "Ganja" : 32,
        "Purohit" : 21

    }

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
async def read_item(student_name):
    return {"student_name" : student_name}


