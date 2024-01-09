
import faker
import sqlite3
from pprint import pprint
from random import randint
from datetime import datetime, date, timedelta


NUMBER_STUDENTS = 100
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


fake = faker.Faker()
connect = sqlite3.connect("hw6.db")
cur = connect.cursor()


def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(teacher_name) VALUES(?);"
    cur.executemany(sql, zip(teachers, ))


def seed_disciplines():
    sql = "INSERT INTO disciplines (discipline_name, teacher_id) VALUES(?, ?);"
    cur.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines)))))


def seed_groups():
    sql = "INSERT INTO groups(group_name) VALUES(?);"
    cur.executemany(sql, zip(groups, ))


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = "INSERT INTO students(student_name, group_id) VALUES(?, ?);"
    cur.executemany(sql, zip(students, iter(randint(1, NUMBER_GROUPS) for _ in range(len(students)))))


def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date =  datetime.strptime("2023-05-25", "%Y-%m-%d")
    sql = "INSERT INTO grades(discipline_id, student_id, grade, date_off) VALUES(?, ?, ?, ?);"

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
        for students in random_students :
            grades.append((random_discipline, students, randint(1,12), day.date()  ))
    cur.executemany(sql, grades )



if __name__ == '__main__':
    try:
        seed_teachers()
        seed_disciplines()
        seed_groups()
        seed_students()
        seed_grades()

        connect.commit()
    except sqlite3.Error as e :
        pprint(e)
    finally:
        connect.close()