from database import Base
from sqlalchemy import Column, Integer,String, Boolean, TIMESTAMP,orm,ForeignKey,DateTime
import datetime as dt

class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer,primary_key = True, nullable = False)
    name = Column(String, nullable = False)
    amount = Column(Integer,nullable = False)
    category = Column(String, default = False)
    created = Column(DateTime,default = dt.datetime.utcnow,nullable = False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = orm.relationship("User")

   
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String)
    email = Column(String,unique = True)
    password = Column(String)

