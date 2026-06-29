from pydantic import BaseModel, Field



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