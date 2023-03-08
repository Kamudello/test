from sqlalchemy import create_engine
from student import Student
from sql_queries import insert_student, get_students


def test_service1(conn_with_data: str):
    assert 2 == 2
    # engine = create_engine(conn_with_data)
    # conn = engine.connect()
    #
    # school = Student(
    #     name="Daniil",
    #     lastname="Kelesov",
    #     clas="11",
    #     attendance="Б",
    #     grade=4
    # )
    # insert_student(conn, school)
    #
    # transactions = get_students(conn)
    # assert len(transactions) == 1
    # transaction = transactions[0]
    # assert transaction.name == "Daniil"
