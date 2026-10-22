# ONLINE EXAMINATION SYSTEM – PROJECT REPORT

## 1. Introduction
The Online Examination System is a web-based application developed using Python and Flask. It allows educational institutions to conduct objective examinations digitally. Students can register, log in, select an active examination, answer multiple-choice questions within a fixed time, and receive an automatically calculated result. Teachers can create examinations and manage questions, while administrators can manage users and monitor the system.

## 2. Objectives
- Conduct examinations online.
- Reduce manual evaluation work.
- Store examination records digitally.
- Provide automatic scoring and result generation.
- Support negative marking.
- Provide student performance history.
- Allow teachers to manage examinations and questions.
- Provide administrators with system-level controls.

## 3. Main Modules
### Student Module
Registration, authentication, dashboard, examination instructions, timed examination, question palette, review marking, automatic submission, result and answer review.

### Teacher Module
Exam creation, exam editing, activation/deactivation, question management, result viewing and Excel export.

### Admin Module
User management, exam overview and dashboard statistics.

## 4. Technologies
Python, Flask, Flask-SQLAlchemy, SQLite, HTML5, CSS3, Bootstrap 5, JavaScript, Pandas and OpenPyXL.

## 5. Database
The system uses User, Exam, Question, Attempt and Answer entities. Relationships connect students to attempts, exams to questions and attempts, and attempts to individual answers.

## 6. Security
Passwords are stored using Werkzeug password hashing. Role-based route protection prevents students, teachers and administrators from accessing unauthorized modules. Flask sessions are used for authentication.

## 7. Examination Process
A student logs in, views active examinations, reads instructions and starts an examination. An Attempt record is created and the timer starts. Answers are submitted to the server. The server compares selected answers with correct answers, calculates positive and negative marks, stores every answer, calculates percentage and determines pass/fail status.

## 8. Future Scope
Future versions can add email notifications, PDF certificates, question import from Excel, scheduled examinations, advanced analytics, REST APIs, MySQL/PostgreSQL deployment, proctoring integrations and cloud hosting.

## 9. Conclusion
The project demonstrates how Python can be used to create a complete database-driven web application. It combines authentication, CRUD operations, database relationships, timed assessments, automated evaluation and data export into a practical educational system.
