from sqlalchemy import create_engine, func, and_
from sqlalchemy.orm import sessionmaker
from src.models import Student, Subject, Grade, Group, Teacher
from src.db import session

# Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    query = session.query(Student).join(Grade).group_by(Student).order_by(func.avg(Grade.grade).desc()).limit(5)
    result = query.all()
    print("Список 5 студентів із найбільшим середнім балом з усіх предметів:")
    for student in result:
        print(student.name)
    print()

# Знайти студента із найвищим середнім балом з певного предмета
def select_2(subject_name):
    query = session.query(Student).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student).\
        order_by(func.avg(Grade.grade).desc()).limit(1)
    result = query.first()
    if result:
        print(f"Студент з найвищим середнім балом з предмета {subject_name}: {result.name}")
    else:
        print(f"Не знайдено студента з предмета {subject_name}")
    print()

# Знайти середній бал у групах з певного предмета
def select_3(subject_name):
    result = session.query(Subject.name, Group.name, func.avg(Grade.grade))\
        .select_from(Grade).join(Student).join(Subject).join(Group)\
        .filter(Subject.name == subject_name).group_by(Subject.name, Group.name).all()
    print(result)
    return result

# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    result = session.query(func.avg(Grade.grade)).select_from(Grade).all()
    print(result)
    return result

# Знайти, які курси читає певний викладач.
def select_5(teacher_id):
    result = session.query(Subject.name).select_from(Subject).join(Teacher).filter(Teacher.id == teacher_id).all()
    print(result)
    return result

# Знайти список студентів у певній групі
def select_6(group_id):
    result = session.query(Student.name).select_from(Student).join(Group).filter(Group.id == group_id).all()
    print(result)
    return result

# Знайти оцінки студентів в окремій групі з певного предмета
def select_7(group_id, subject_name):
    result = session.query(Student.name, Grade.grade).select_from(Grade).join(Student).join(Subject).join(Group)\
        .filter(Group.id == group_id, Subject.name == subject_name).all()
    print(result)
    return result

# Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(teacher_id):
    result = session.query(Teacher.name, Subject.name, func.avg(Grade.grade))\
        .select_from(Grade).join(Student).join(Subject).join(Teacher)\
        .filter(Teacher.id == teacher_id).group_by(Teacher.name, Subject.name).all()
    print(result)
    return result

# Знайти список курсів, які відвідує певний студент
def select_9(student_id):
    result = session.query(Subject.name).select_from(Subject).join(Grade).join(Student)\
        .filter(Student.id == student_id).group_by(Subject.name).all()
    print(result)
    return result

# Список курсів, які певному студенту читає певний викладач
def select_10(student_id, teacher_id):
    result = session.query(Subject.name).select_from(Subject).join(Grade).join(Student).join(Teacher)\
        .filter(Student.id == student_id, Teacher.id == teacher_id).group_by(Subject.name).all()
    print(result)
    return result

# Середній бал, який певний викладач ставить певному студентові
def select_11(teacher_id, student_id):
    result = session.query(func.avg(Grade.grade)).select_from(Grade)\
        .join(Student).join(Subject).join(Teacher)\
        .filter(and_(Teacher.id == teacher_id, Student.id == student_id)).first()
    return round(float(result[0]), 4)

# Оцінки студентів у певній групі з певного предмета на останньому занятті
def select_12(group_id, subject_name):
    result = session.query(Student.name, Grade.grade).select_from(Grade).join(Student).join(Subject).join(Group)\
        .filter(Group.id == group_id, Subject.name == subject_name).order_by(Grade.date.desc()).all()
    print(result)
    return result

if __name__ == "__main__":
    select_1()
    select_2('Фізика')
    select_3('Хімія')
    select_4()
    select_5(3)
    select_6(1)
    select_7(1, 'Математика')
    select_8(2)
    select_9(9)
    select_10(4, 3)
    print(select_11(3, 4))
    select_12(1, 'Фізика')

