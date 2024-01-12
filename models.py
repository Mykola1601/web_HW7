
from db import engine
from sqlalchemy.orm import  DeclarativeBase, relationship
from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, func, event
from sqlalchemy.ext.hybrid import hybrid_property

class Base(DeclarativeBase):
    pass


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), unique = True)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100))


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100))
    group_id = Column('group_id',Integer, ForeignKey('groups.id'))
    # discipline = relationship('Discipline')

class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100))
    teacher_id = Column('teacher_id',Integer, ForeignKey('teachers.id'))
    # teacher = relationship('Teacher')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer(), primary_key=True)
    discipline_id = Column( 'discipline_id',Integer, ForeignKey('disciplines.id'))
    student_id = Column( 'student_id',Integer, ForeignKey('students.id'))
    grade = Column("grade", Integer())
    date_off = Column(DateTime)
    # create_at = Column(DateTime, default = func.now())
    # updated_at = Column(DateTime, default = func.now())
    student = relationship('Student')
    discipline = relationship('Discipline')


# @event.listens_for(Grade, "before_update")
# def update_updated_at(mapper, conn, target):
#     target.updated_at = func.now()



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine




