from sqlalchemy import create_engine
# from psycopg2._psycopg import connection
# import psycopg2
#
# conn: connection = psycopg2.connect(
#     host="test.dsacademy.kz",
#     database="fortesting",
#     user="testing",
#     password="testing123"
# )


engine = create_engine("postgresql+psycopg2://testing:testing123@test.dsacademy.kz:5432/fortesting")
conn = engine.connect()