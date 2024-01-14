
from sqlalchemy import and_
from db import session
from models import Student, Teacher, Grade, Group, Discipline



def create(model, name, id):
    if model == "Teacher":
        data = Teacher(name = name)
    if model == "Group":
        data = Group(name = name)
    if model == "Student":
        data = Student(name = name)
    if model == "Discipline":
        data = Discipline(name = name)

    session.add(data)
    session.commit()
    session.close()


def read(model, name, id):
    if model == "Teacher":
        data = Teacher
    if model == "Group":
        data = Group
    if model == "Student":
        data = Student
    if model == "Discipline":
        data = Discipline
    if model == "Grade":
        data = Grade

    result = session.query("*") \
         .select_from(data)\
         .all()
    session.commit()
    session.close()
    return result


def update(model, name, id):
    if model == "Teacher":
        data = Teacher
    if model == "Group":
        data = Group
    if model == "Student":
        data = Student
    if model == "Discipline":
        data = Discipline

    result = session.query(data).get(int(id))
    result.name = name
    session.add(result)
    session.commit()
    return  result


def delete(model, name, id):
    if model == "Teacher":
        data = Teacher
    if model == "Group":
        data = Group
    if model == "Student":
        data = Student
    if model == "Discipline":
        data = Discipline
    
    result = session.query(data).get(int(id))
    session.delete(result)
    session.commit()
    return result




if __name__ == '__main__':
    pass






