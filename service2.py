import time
from sql_queries import create_table, update_students_good
from student import Student
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        update_students_good(conn)
        print("Updated")
        time.sleep(1)
