from sqlalchemy import Column, ForeignKey, Integer, String,Boolean,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()


# basic data managment 3.1.1
class Building(Base):
    __tablename__ ='building'
    id = Column(Integer, primary_key = True)
    code =Column(String(40), nullable = False)
    description =Column(String(150), nullable = False)
    availability = Column(Boolean, nullable = False)

class Floor(Base):
    __tablename__ = 'floor'
   
    id = Column(Integer, primary_key=True)
    code = Column(String(250), nullable=False)
    description =Column(String(150), nullable = False)
    availability = Column(Boolean, nullable = False)   
    # hight discribes floor number
    # hieght = Column(Integer ,nullable = False)

    # building containing this floor
    building_id = Column(Integer , ForeignKey('building.id'))
    building = relationship(Building)


class Location(Base):
    __tablename__ ='location'

    id = Column(Integer, primary_key=True)
    code = Column(String(250), nullable=False)
    description =Column(String(150), nullable = False)
    availability = Column(Boolean, nullable = False)

    color = Column(Integer, nullable = False)
    regular_capacity = Column(Integer)
    # capacity for exam time 
    exam_capacity = Column(Integer )
    
    # added from 3.1.2 a SRS
    datashow = Column(Boolean )
    aircondition = Column(Boolean )
    board = Column(Boolean)

    # floor containing this location
    floor_id = Column(Integer , ForeignKey('floor.id'))
    floor = relationship(Floor)

    subjects = relationship("Subject",
                            secondary='location_subject',
                            back_populates="location")

# 
class Department(Base):
    __tablename__ ='department'

    id = Column(Integer, primary_key=True)
    code = Column(String(250), nullable=False)
    name =Column(String(150), nullable = False)

    # department building
    building_id = Column(Integer , ForeignKey('building.id'))
    building = relationship(Building)
   

class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    position = Column(String(10))

    department_id = Column(Integer , ForeignKey('department.id'))
    department = relationship(Department)
   
class Subject(Base):
    __tablename__ = 'subject'
    id= Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
# ?abdo ragab think it is lecture time in minute 
    lecture_time = Column(Integer)

# ?abdo ragab subject may have many departments why one-many relation
    department_id = Column(Integer , ForeignKey('department.id'))
    department = relationship(Department)

    # you me not care about this it is just for implementing curd with session
    # it is not important for database creation 
    location = relationship(
                        "Location",
                        secondary='location_subject',
                        back_populates="subjects")

# table to relate location and subjects
location_subject = Table('location_subject', Base.metadata,
    Column('subject_id', Integer, ForeignKey('subject.id')),
    Column('location_id', Integer, ForeignKey('location.id'))
)    

# to generate data base for sqlite (working)
engine = create_engine('sqlite:///lte01_oracle.db')
#  to generate for oracle
# engine = create_engine('oracle+cx_oracle://username:password@host:port/database')


Base.metadata.create_all(engine)

# to generate uml code plantuml use vscode extention
# http://www.plantuml.com
# if __name__ == '__main__':
#     import codecs
#     import sadisplay

#     desc = sadisplay.describe(globals().values())

#     with codecs.open('schema.plantuml', 'w', encoding='utf-8') as f:
#         f.write(sadisplay.plantuml(desc))
