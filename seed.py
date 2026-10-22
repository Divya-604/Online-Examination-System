from app import create_app, db
from models import User, Exam, Question

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    admin = User(name="System Admin", email="admin@example.com", username="admin", role="admin")
    admin.set_password("admin123")

    teacher = User(name="Demo Teacher", email="teacher@example.com", username="teacher", role="teacher")
    teacher.set_password("teacher123")

    student = User(name="Demo Student", email="student@example.com", username="student",
                   role="student", course="B.Com", roll_number="BCOM001")
    student.set_password("student123")

    db.session.add_all([admin, teacher, student])
    db.session.commit()

    exam = Exam(
        name="Python Programming Basics",
        subject="Python",
        description="A demo examination covering Python fundamentals.",
        duration=20,
        marks_per_question=1,
        negative_marks=0.25,
        passing_marks=5,
        is_active=True,
        created_by=teacher.id
    )
    db.session.add(exam)
    db.session.commit()

    questions = [
        ("Which keyword is used to define a function in Python?", "function", "def", "fun", "define", "B", "The def keyword defines a function.", "Easy"),
        ("Which data type is immutable?", "List", "Dictionary", "Tuple", "Set", "C", "Tuples are immutable.", "Easy"),
        ("Which symbol is used for a single-line comment?", "//", "#", "/*", "<!--", "B", "Python uses # for comments.", "Easy"),
        ("What is the output type of input() in Python 3?", "int", "float", "string", "boolean", "C", "input() returns a string by default.", "Easy"),
        ("Which method adds an item to the end of a list?", "add()", "append()", "push()", "insertEnd()", "B", "append() adds an item to the end.", "Easy"),
        ("Which keyword is used for exception handling?", "try", "catch", "error", "exceptonly", "A", "A try block contains code that may raise an exception.", "Easy"),
        ("Which library is commonly used for data analysis?", "Pandas", "Flask", "Tkinter", "Socket", "A", "Pandas is widely used for data analysis.", "Easy"),
        ("What does len() return?", "Memory address", "Length/number of items", "Data type", "Last element", "B", "len() returns the number of items.", "Easy"),
        ("Which operator performs exponentiation?", "^", "//", "**", "%%", "C", "The ** operator performs exponentiation.", "Easy"),
        ("Which collection stores key-value pairs?", "List", "Tuple", "Dictionary", "Set", "C", "Dictionaries store key-value pairs.", "Easy"),
    ]

    for q in questions:
        db.session.add(Question(
            exam_id=exam.id, question_text=q[0],
            option_a=q[1], option_b=q[2], option_c=q[3], option_d=q[4],
            correct_answer=q[5], explanation=q[6], difficulty=q[7]
        ))
    db.session.commit()
    print("Database created successfully.")
    print("Admin: admin / admin123")
    print("Teacher: teacher / teacher123")
    print("Student: student / student123")
