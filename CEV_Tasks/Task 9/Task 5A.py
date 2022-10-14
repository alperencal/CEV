from numpy import np
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from faker import Faker
import time

Base = declarative_base()
#I created a new DataBase which has named as hwdb
engine = create_engine("postgresql://postgres:postgres@localhost:5432/hwdb") 
session = sessionmaker(bind = engine)

class Table(Base):
    __tablename__ = "Login"
    id = Column(Integer, primary_key = "True")
    email = Column(String(50))
    password = Column(String(50), nullable = "False")

class Table_2(Base): 
    __tablename__ = "Finding"
    id = Column(Integer, primary_key = "True")
    email = Column(String(50))
    password = Column(String(50), nullable = "False")

Base.metadata.create_all(engine)   

def fake_generate(i): # i given as 10000 in HW.
    empty_list = []
    for i in range(i):
        fake = Faker()
        list_1 = []
        list_1.append(fake.email())
        list_1.append(fake.password())
        empty_list.append(list_1)    
    return empty_list    

session.commit()


start_time = time.time()

"""
loop
"""

end_time = time.time()
print((end_time)-(start_time))            


