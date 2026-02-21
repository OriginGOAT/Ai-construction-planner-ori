from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer,primary_key=True,index=True)
    location = Column(String)
    project_type = Column(String)
    soil = Column(String)
    workers = Column(Integer)
    cement = Column(Integer)
    excavators = Column(Integer)
    steel = Column(Integer)
    budget = Column(Integer)
