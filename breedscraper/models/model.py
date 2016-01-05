
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
 
class Source(Base):
    __tablename__ = 'Sources'
    # Here we define columns for the table source
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class Breed(Base):
    __tablename__ = 'Breeds'
    # Here we define columns for the table breeds.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(Text)
    source_avatar = Column(Text, nullable=True)
    local_avatar = Column(Text, nullable=True)
    SourceId = Column(Integer, ForeignKey('Sources.id'))
    source = relationship(Source)