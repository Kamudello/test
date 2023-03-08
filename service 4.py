import time
from sql_queries import create_table, get_students
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        students = get_students(conn)
        for student in students:
            print(student)
        time.sleep(100)