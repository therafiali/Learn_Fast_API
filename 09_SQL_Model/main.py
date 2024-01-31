from typing import Optional
from sqlmodel import SQLModel, Field, create_engine

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None
    
    
database_connection_str = "postgresql://postgres:rootadmin@localhost:5432/SQL_Model"    
#echo true only development env not for production
engine = create_engine(database_connection_str, echo=True)    

SQLModel.metadata.create_all(engine)