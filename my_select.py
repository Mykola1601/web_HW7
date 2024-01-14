
from db import session  
from models import Student, Teacher, Grade, Group, Discipline
from sqlalchemy import select, func, desc,   table, column
from pprint import pprint


def select_1():
   result = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade') )\
      .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')) .limit(5).all()
   return result


def select_2(discipline_id):
   res = session.query(
      Discipline.name,
      Student.name,
      func.round(func.avg(Grade.grade), 2).label("avg_grade") ) \
         .select_from(Grade)\
         .join(Student).join(Discipline)\
         .filter(Discipline.id == discipline_id)\
         .group_by(Student.name, Discipline.name)\
         .order_by(desc("avg_grade"))\
         .limit(1).all()
   return res


def select_3(discipline_id):
   res = session.query(
      Group.name,
      Discipline.name,
      func.round(func.avg(Grade.grade), 2).label("avg_grade") ) \
         .select_from(Grade)\
         .join(Student)\
         .join(Discipline)\
         .join(Group)\
         .filter(Discipline.id == discipline_id)\
         .group_by(Group.name, Discipline.name)\
         .order_by(desc("avg_grade"))\
         .all()
   return res


def select_4():
   res = session.query(
      func.round(func.avg(Grade.grade), 2).label("avg_grade") ) \
         .select_from(Grade)\
         .all()
   return res


def select_5(teacher_id):
   res = session.query(
      Teacher.name,
      Discipline.name ) \
         .select_from(Grade)\
         .join(Student)\
         .join(Discipline)\
         .join(Group)\
         .join(Teacher)\
         .filter(Teacher.id == teacher_id)\
         .group_by(Teacher.name, Discipline.name)\
         .all()
   return res


def select_6(group_id):
   res = session.query(
      Student.name,
      Group.name ) \
         .select_from(Student)\
         .join(Group)\
         .filter(Group.id == group_id)\
         .all()
   return res


def select_7(group_id, discipline_id):
   res = session.query(
      Student.name,
      # Group.name,
      # func.count('*').label("num"),  \
      Grade.grade ) \
         .select_from(Grade)\
         .join(Student)\
         .join(Discipline)\
         .join(Group)\
         .filter((Group.id == group_id) , (Discipline.id == discipline_id))\
         .order_by(Student.name)\
         .all()
   return res


def select_8(teacher_id):
   res = session.query(
      Teacher.name,
      Discipline.name,
      func.round(func.avg(Grade.grade), 2).label("avg_grade") ) \
         .select_from(Grade)\
         .join(Discipline)\
         .join(Teacher)\
         .filter(Teacher.id == teacher_id)\
         .group_by(Teacher.name, Discipline.name)\
         .all()
   return res


def select_9(student_id):
   res = session.query(
      Student.name,
      Discipline.name
          ) \
         .select_from(Grade)\
         .join(Discipline)\
         .join(Student)\
         .filter(Student.id == student_id)\
         .group_by(Student.name, Discipline.name)\
         .order_by(Discipline.name)\
         .all()
   return res


def select_10(student_id, teacher_id):
   res = session.query(
      # Student.name,
      # Discipline.teacher_id,
      Discipline.name
          ) \
         .select_from(Grade)\
         .join(Discipline)\
         .join(Student)\
         .filter(Discipline.teacher_id == teacher_id, Grade.student_id == student_id )\
         .group_by( Student.name, Discipline.name, Discipline.id)\
         .order_by(Discipline.name)\
         .all()
   return res


def select_11( teacher_id, student_id):
   res = session.query(
      Student.name,
      Teacher.name,
      func.round(func.avg(Grade.grade), 2).label("avg_grade") ) \
         .select_from(Grade)\
         .join(Discipline)\
         .join(Student)\
         .join(Teacher)\
         .filter(Discipline.teacher_id == teacher_id, Grade.student_id == student_id )\
         .group_by( Student.name, Teacher.name)\
         .all()
   return res


def select_12(discipline_id, group_id):
   subquery = ( 
      select(Grade.date_off)\
      .join(Student).join(Group)\
      .where((Grade.discipline_id == discipline_id) and (Group.group_id == group_id))\
      .order_by(desc(Grade.date_off)).limit(1).scalar_subquery() )
        

   res = session.query(
      Discipline.name,
      Group.name,
      Student.name,
      Grade.grade,
      Grade.date_off ) \
         .select_from(Grade)\
         .join(Student).join(Discipline).join(Group).join(Teacher)\
         .where(Discipline.id == discipline_id, Group.id == group_id, Grade.date_off == subquery )\
         .group_by(Grade.grade, Grade.date_off, Discipline.name, Student.name, Group.name)\
         .order_by(Grade.grade)\
         .all()
          
   return res




if __name__ == '__main__':
   # pprint(select_1())
   # pprint(select_2(1))
   # pprint(select_3(3))
   # pprint(select_4())
   # pprint(select_5(1))
   # pprint(select_6(3))
   # pprint(select_7(3, 3))
   # pprint(select_8(1))
   # pprint(select_9(32))
   # pprint(select_10(15,5))
   # pprint(select_11(1, 94))
   pprint(select_12(2, 3))
   print('\n\n')


