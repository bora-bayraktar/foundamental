from sqlalchemy import Column, Integer, Float, String, BigInteger 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Deal(Base):
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(BigInteger)
    funding_amount = Column(Float)
    funding_round = Column(String)
    company_id = Column(Integer)