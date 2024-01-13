
from db import engine
from sqlalchemy.orm import  declarative_base, relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey, Date, func
from sqlalchemy.ext.hybrid import hybrid_property

# class Base(DeclarativeBase):
#     pass
Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100),  nullable = False)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable = False)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable = False)
    group_id = Column('group_id', ForeignKey('groups.id', ondelete = 'CASCADE'))
    group = relationship('Group', backref = "students")

class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable = False)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete = 'CASCADE'))
    teacher = relationship('Teacher' , backref = "disciplines")


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer(), primary_key=True)
    grade = Column("grade", Integer())
    discipline_id = Column( 'discipline_id',Integer, ForeignKey('disciplines.id', ondelete = 'CASCADE'))
    student_id = Column( 'student_id',Integer, ForeignKey('students.id', ondelete = 'CASCADE'))
    date_off = Column(Date, nullable = False)
    student = relationship('Student', backref = "grade")
    discipline = relationship('Discipline', backref = "grade")


# @event.listens_for(Grade, "before_update")
# def update_updated_at(mapper, conn, target):
#     target.updated_at = func.now()



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine




