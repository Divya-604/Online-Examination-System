# Online Examination System

A complete college-level Online Examination System built with Python, Flask, SQLite, HTML, CSS and JavaScript.

## Features

### Student
- Registration and login
- Student dashboard
- Available examinations
- Instructions before starting
- Countdown timer
- MCQ examination interface
- Next/Previous navigation
- Question palette
- Mark for review
- Clear answer
- Automatic submission when time expires
- Automatic evaluation
- Negative marking
- Detailed result
- Answer review with explanations
- Previous exam history
- Performance chart

### Teacher
- Teacher dashboard
- Create exams
- Edit/delete exams
- Add/edit/delete questions
- Set duration, marks, negative marking and passing marks
- Activate/deactivate exams
- View student attempts
- Export results to Excel

### Admin
- Admin dashboard
- Manage users
- View exams and attempts
- Delete users
- System statistics

## Demo Accounts

Admin:
- Username: admin
- Password: admin123

Teacher:
- Username: teacher
- Password: teacher123

Student:
- Username: student
- Password: student123

## Run

1. Install Python 3.10+.
2. Open terminal in this project folder.
3. Run:

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

4. Install packages:

```bash
pip install -r requirements.txt
```

5. Create database and sample data:

```bash
python seed.py
```

6. Start server:

```bash
python app.py
```

7. Open:
http://127.0.0.1:5000

## Project Structure

- `app.py` - Flask application and routes
- `models.py` - database models
- `seed.py` - demo database/data
- `app/templates/` - HTML pages
- `app/static/` - CSS and JavaScript
- `exports/` - generated Excel result files

The project uses SQLite so it works immediately without installing MySQL.
