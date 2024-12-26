import random
from datetime import datetime, timedelta
from faker import Faker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Student, Group, Teacher, Subject, Grade

DATABASE_URL = "postgresql+psycopg2://username:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

def seed_database():
    groups = [Group(name=f"Group {i+1}") for i in range(3)]
    session.add_all(groups)

    teachers = [Teacher(name=faker.name()) for _ in range(5)]
    session.add_all(teachers)

    subjects = [
        Subject(name=faker.word(), teacher=random.choice(teachers))
        for _ in range(8)
    ]
    session.add_all(subjects)

    students = [
        Student(name=faker.name(), group=random.choice(groups))
        for _ in range(50)
    ]
    session.add_all(students)

    for student in students:
        for subject in subjects:
            for _ in range(random.randint(1, 20)):
                grade = Grade(
                    value=random.uniform(1, 5),
                    date=faker.date_this_year(),
                    student=student,
                    subject=subject,
                )
                session.add(grade)

    session.commit()

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    seed_database()