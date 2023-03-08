from sqlalchemy.engine import Connection
from sqlalchemy import text

from student import Student


def create_table(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS student_1 (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        clas VARCHAR(255) NOT NULL,
        attendance VARCHAR(255) NOT NULL,
        grade INTEGER
        )
    """

    conn.execute(text(query))
    conn.commit()


def insert_student(conn: Connection, student: Student):
    query = """
    INSERT INTO student_1 (name, lastname, clas, attendance, grades)
    VALUES (:name, :lastname, :clas, :attendance, :grade);
    """

    conn.execute(
        text(query),
        parameters={
            "name": student.name,
            "lastname": student.lastname,
            "clas": student.clas,
            "attendance": student.attendance,
            "grade": student.grade
        },
    )
    conn.commit()


def update_students_good(conn: Connection):
    query = "UPDATE student_1 SET grade=5 WHERE attendance='Б';"
    conn.execute(text(query))
    conn.commit()


def update_students_bad(conn: Connection):
    query = "UPDATE student_1 SET grade=2 WHERE attendance='Н';"
    conn.execute(text(query))
    conn.commit()


def get_students(conn: Connection) -> list[Student]:
    query = "SELECT * FROM transactions;"
    print("ddd")
    students = conn.execute(text(query)).fetchall()
    print("ddd1")
    return [Student(
        id=student[0],
        name=student[1],
        lastname=student[2],
        clas=student[3],
        attendance=student[4],
        grade=student[5]
    ) for student in students]
