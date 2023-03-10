from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = "companies"
    
    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    country = Column(String(255))
    founding_date = Column(DateTime)
    description = Column(String(255))
