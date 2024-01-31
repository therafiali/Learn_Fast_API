from typing import Optional
from sqlmodel import SQLModel, Field, create_engine,Session

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
    
    
database_connection_str = "postgresql://postgres:rootadmin@localhost:5432/SQL_Model"    
#echo true only development env not for production
engine = create_engine(database_connection_str, echo=True)    

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_hero():
    hero1 = Hero(name="Rafi Ali",secret_name="Rafay",age=22)
    hero2 = Hero(name="Abu Bakr",secret_name="Sadiq",age=42)
    hero3 = Hero(name="Umer",secret_name="Farooq",age=32)
    
    session = Session(engine)
    session.add(hero1)
    session.add(hero2)
    session.add(hero3)
    session.commit()
    session.close()
    
    
if __name__ == "__main__":
    create_db_and_tables()
    create_hero()
