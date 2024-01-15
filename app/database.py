from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import setting
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#TO RUN RAW SQL
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='FastAPI', user='postgres', password='Password$1234', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection was sucessfull!')
#         break

#     except Exception as error:
#         print('Connection to Database failed')
#         print('Error: ', error)
#         time.sleep(5)