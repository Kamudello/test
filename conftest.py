from typing import Generator
import pytest
from sqlalchemy import create_engine
from testcontainers.postgres import PostgresContainer

from sql_queries import create_table, insert_student
from student import Student


@pytest.fixture()
def postgres_container1() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer(image="postgres:latest") as container:
        container.start()
        yield container


@pytest.fixture()
def postgres_container() -> PostgresContainer:
    container = PostgresContainer(image="postgres:latest")
    container.start()
    return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    return postgres_container.get_connection_url()


@pytest.fixture(scope="function")
def conn_with_data(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    students = [
        Student(
            name="Daniil",
            lastname="Kelesov",
            clas="11",
            attendance="Б",
            grade=4
        ),
        Student(
            name="Daniil1",
            lastname="Kelesov1",
            clas="111",
            attendance="Б1",
            grade=3
        ),
        Student(
            name="Daniil2",
            lastname="Kelesov2",
            clas="112",
            attendance="Б2",
            grade=2
        ),
    ]
    for student in students:
        insert_student(conn, student)
    return postgres_container.get_connection_url()
