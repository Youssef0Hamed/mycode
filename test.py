# from typing import Union
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# class Item(BaseModel):
#     id:int 
#     name: str
#     grade: str 
#     age: int 
    

# students_db = [
#     Item(id=1, name="Youssef", grade="A", age=19),
#     Item(id=2, name="Lina", grade="B", age=20),
#     Item(id=3, name="Ahmed", grade="A", age=18),
#     Item(id=4, name="Sara", grade="C", age=21),
#     Item(id=5, name="Omar", grade="B", age=22),
# ]
# app = FastAPI()

# @app.get("/api/studnt/")
# def read_root():
#     return students_db


# @app.get("/api/studnt/${id}")                  # to show data 
# def read_item(id: int,):
#     return  students_db[id-1]

# @app.post("/api/studnt/")                       # to add data 
# def add_studnt(id: int , studnt : Item ):  
#     # for i in students_db:
#     #     for id in students_db[i]:
    
#     students_db.append(studnt)
#     return students_db

# @app.put("/api/studnt/${id}/")
# def edit_studnt(id: int,studnt : Item):
#     students_db[id-1] = studnt.dict()
#     return students_db[id-1]

# @app.delete("/api/studnt/${id}")
# def edit_studnt(id: int):
#     deleted_student  = students_db.pop(id-1)
#     return  {"message": "Student deleted successfully", "student": deleted_student}

import pandas as pd

# df = pd.DataFrame({
#     "names" : ["Alice", "Bob", "Charlie"],
#     "ages" : [25, 30, 35]
# })
df = pd.read_csv('salary-dataset.csv')

s = df["salary"].skew()
w = df["salary"].mean()
x= df["salary"].describe()
print(s)
print(w)
print(x)

def X (series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return series[(series < lower_bound) | (series > upper_bound)]
outliers = X(df["salary"])
print("Outliers in salary column:")



haljhbdfb
lkjdbfb
ljhbsEIUFB
