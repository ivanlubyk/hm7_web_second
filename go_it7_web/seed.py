from faker import Faker
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Student, Group, Teacher, Subject, Grade

from src.db import session
import random
from sqlalchemy import func


# Ініціалізація Faker для української мови
fake = Faker('uk_UA')

# Створення студентів
students_count = 50
for _ in range(students_count):
    student = Student(name=fake.name(), group_id=random.randint(1, 3))
    session.add(student)
session.commit()

# Створення груп
groups = ['Група 1', 'Група 2', 'Група 3']
for group_name in groups:
    group = Group(name=group_name)
    session.add(group)
session.commit()

# Створення викладачів
teachers_count = 5
for _ in range(teachers_count):
    teacher = Teacher(name=fake.name())
    session.add(teacher)
session.commit()

# Створення предметів та призначення викладачів
subjects = ['Математика', 'Фізика', 'Хімія', 'Історія', 'Географія', 'Біологія', 'Англійська мова']
for subject_name in subjects:
    teacher = session.query(Teacher).order_by(func.random()).first()
    subject = Subject(name=subject_name, teacher=teacher)
    session.add(subject)
session.commit()

# Заповнення оцінок для кожного студента з усіх предметів
students = session.query(Student).all()
subjects = session.query(Subject).all()
grades_count = 20
for student in students:
    for _ in range(grades_count):
        subject = random.choice(subjects)
        grade = Grade(student=student, subject=subject, grade=random.randint(1, 12), date=datetime.now())
        session.add(grade)
session.commit()

# Закриття сесії
session.close()

if __name__ == "__main__":
    students_count = 50
    for _ in range(students_count):
        student = Student(name=fake.name(), group_id=random.randint(1, 3))
        session.add(student)
    session.commit()
