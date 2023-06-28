from faker import Faker
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Student, Group, Teacher, Subject, Grade

import random
from sqlalchemy import func

# Створення бази даних та сесії SQLAlchemy
engine = create_engine('postgresql+psycopg2://postgres:88888888@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()