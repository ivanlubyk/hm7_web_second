from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column('group_id', ForeignKey('groups.id'))
    group = relationship('Group', backref='students')
    #grades = relationship('Grade', back_populates='students')

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    #students = relationship('Student', back_populates='groups')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # subjects = relationship('Subject', back_populates='teachers')

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id'))
    teacher = relationship('Teacher', backref='subjects')
    # grades = relationship('Grade', back_populates='subjects')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column('student_id', ForeignKey('students.id'))
    subject_id = Column('subject_id', ForeignKey('subjects.id'))
    grade = Column(Integer)
    date = Column(DateTime)
    student = relationship('Student', backref='grades')
    subject = relationship('Subject', backref='grades')

