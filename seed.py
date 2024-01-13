
from faker import Faker
from db import session
from random import randint, choice
from datetime import datetime, date, timedelta
from models import Student, Teacher, Grade, Group, Discipline


NUMBER_STUDENTS = 200
NUMBER_TEACHERS = 5
NUMBER_GROUPS = 3
NUMBER_DISCIPLINES = 7


disciplines = [
    "математика",
    "геометрія",
    "програмвання",
    "англійська",
    "географія",
    "креслення",
    "історія",
]

groups = [
    "e12",
    "t13",
    "r10",
]


fake = Faker()


def seed_teachers():
    for _ in range(NUMBER_TEACHERS):
        teacher = Teacher(
            name = fake.name()
        )
        session.add(teacher)
    session.commit()


def seed_groups():
    for i in groups:
        group = Group(
            name = i
        )
        session.add(group)
    session.commit()


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    for i in students:
        student = Student(
            name = i,
            group_id=randint(1, NUMBER_GROUPS)
        )
        session.add(student)
    session.commit()


def seed_disciplines():
    for i in  disciplines:
        discipline = Discipline(
            name=i,
            teacher_id=randint(1, NUMBER_TEACHERS)
        )
        session.add(discipline )
    session.commit()


def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date =  datetime.strptime("2023-05-25", "%Y-%m-%d")

    def get_dates(start:date, end:date):
        result = []
        cur_date = start
        while cur_date <= end:
            if cur_date.isoweekday() < 6:
                result.append(cur_date)
            cur_date += timedelta(1)
        return result
    list_dates = get_dates(start_date, end_date)

    grades = []
    for day in list_dates:
        random_discipline = randint(1,len(disciplines))
        random_students = [ randint(1, NUMBER_STUDENTS) for _ in range(20) ]
        for student in random_students :
            grade= Grade(
                discipline_id=randint(1, NUMBER_DISCIPLINES),
                student_id=student,
                grade=randint(2,12),
                date_off=day.date() ,
            )
            session.add(grade)
    session.commit()


if __name__ == '__main__':
    try:
        seed_groups()
        seed_teachers()
        seed_disciplines()
        seed_students()
        seed_grades()
    except :
        print("error")
    finally:
        session.close()