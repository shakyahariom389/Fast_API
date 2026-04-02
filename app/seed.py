from datetime import datetime
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app.models import Base, Student, Course, Enrollment

def seed_data(db: Session):

    # If data already exists, stop
    if db.query(Student).first():
        print("Data already exists")
        return

    # Students
    students = [
        Student(name="Rahul", grade="A", created_at=datetime.now()),
        Student(name="Priya", grade="B", created_at=datetime.now()),
        Student(name="Amit", grade="A", created_at=datetime.now()),
        Student(name="Neha", grade="C", created_at=datetime.now()),
        Student(name="Ravi", grade="B", created_at=datetime.now()),
        Student(name="Anita", grade="A", created_at=datetime.now()),
        Student(name="Vikas", grade="C", created_at=datetime.now()),
        Student(name="Pooja", grade="B", created_at=datetime.now()),
        Student(name="Arjun", grade="A", created_at=datetime.now()),
        Student(name="Kiran", grade="B", created_at=datetime.now())
    ]

    # Courses
    courses = [
        Course(name="Mathematics", category="Science"),
        Course(name="Physics", category="Science"),
        Course(name="History", category="Arts"),
        Course(name="Computer Science", category="Technology"),
        Course(name="English", category="Language"),
        Course(name="PYTHON", category="Technology")
    ]

    db.add_all(students)
    db.add_all(courses)
    db.commit()

    # Enrollments
    enrollments = []

    for i in range(20):
        enrollments.append(
            Enrollment(
                student_id=(i % 10) + 1,
                course_id=(i % 5) + 1,
                enrolled_at=datetime.now()
            )
        )

    db.add_all(enrollments)
    db.commit()

    print("Database seeded successfully!")


if __name__ == "__main__":

    # Create tables
    Base.metadata.create_all(bind=engine)

    # Create session
    db = SessionLocal()

    # Seed data
    seed_data(db)

    # Close session
    db.close()