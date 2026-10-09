from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
from .config import settings
#first we were basically harcoding the values but now we have stored that information in environment variables and we will use that now so that everyone cann't seee our passwordsa and username
SQLALCHEMY_DATABASE_URL=f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

while True:
#it  may happen that sometimes the connection with databases might fail and so we are creating this try statement
    try:
        conn=psycopg2.connect(host='localhost', database='fastapi', user='postgre', password='password',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was successful")
        break
#host==the IP adress over here when we will be importing then column names don't come so we will have to import them too
    except Exception as error:
        print("Connecting to databse failed")
        print("Error: ",error)
        time.sleep(2) #whenever it has an error i want it to wait for some time before reconnecting
 
