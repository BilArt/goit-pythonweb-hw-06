from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func, desc
from models import Student, Group, Teacher, Subject, Grade

DATABASE_URL = "postgresql+psycopg2://username:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    return session.query(Student.name, func.avg(Grade.value).label('average'))\
        .join(Grade).group_by(Student.id)\
        .order_by(desc('average')).limit(5).all()

def select_2(subject_id):
    return session.query(Student.name, func.avg(Grade.value).label('average'))\
        .join(Grade).filter(Grade.subject_id == subject_id)\
        .group_by(Student.id).order_by(desc('average')).first()

def select_3(subject_id):
    return session.query(Group.name, func.avg(Grade.value).label('average'))\
        .join(Student).join(Grade).filter(Grade.subject_id == subject_id)\
        .group_by(Group.id).all()

def select_4():
    return session.query(func.avg(Grade.value)).scalar()

def select_5(teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

def select_6(group_id):
    return session.query(Student.name).filter(Student.group_id == group_id).all()

def select_7(group_id, subject_id):
    return session.query(Student.name, Grade.value).join(Grade)\
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

def select_8(teacher_id):
    return session.query(func.avg(Grade.value).label('average'))\
        .join(Subject).filter(Subject.teacher_id == teacher_id).scalar()

def select_9(student_id):
    return session.query(Subject.name).join(Grade)\
        .filter(Grade.student_id == student_id).distinct().all()

def select_10(student_id, teacher_id):
    return session.query(Subject.name).join(Grade)\
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).all()