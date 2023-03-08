import time
import random

from sql_queries import create_table, insert_student
from student import Student
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        insert_student(
            conn,
            Student(
                name=random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Emily']),
                lastname=random.choice(['Smith', 'Jones', 'Brown', 'Taylor', 'Wilson']),
                clas=random.choice(['7', '8', '9', '10', '11']),
                attendance=random.choice(["Н", "Б"]),
                grade=random.randint(2, 5)
            )
        )
        print("Inserted")
        time.sleep(1)
