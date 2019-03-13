#/user/bin/env python3.7
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()


# basic data managment 3.1.1
class Building(Base):
    '''
    A- Building: - maintains the faculty building via storing the following information: - 
        
        ✓ Id: Sequential number i.e. 1,2,3…  
        ✓ Code: - unique string that identifies the building i.e. A, B, C … 
        ✓ Description: - string describes the building i.e. Civil Eng Dept 


    # argue (abdo):?? no need for availability here location availability cover this
    # 
    # added v_01
    * availability for inicating if building is available as unavialble means you can't 
        add any thing to building locations 
    '''
    __tablename__ ='building'
    id = Column(Integer, primary_key = True)
    code =Column(String(40), nullable = False)
    description =Column(String(150), nullable = False)
    availability = Column(Boolean, nullable = False)

class Floor(Base):
    '''
    B- Building-Floor: - maintains the faculty building floors via storing the following information:
        ✓ Id: Sequential number i.e. 1,2,3…
        ✓ Code: - unique string that identifies the sub-building i.e. A-1, A-2 …
        ✓ Description: - string describes the building i.e. 1st floor, 2nd floor 

    # added
    * availability for inicating if floor is available
    ?? no need for it location give this info
    ## relations
    * building_id - floor has one to one relation with building 
    '''
    __tablename__ = 'floor'
   
    id = Column(Integer, primary_key=True)
    code = Column(String(250), nullable=False)
    description =Column(String(150), nullable = False)
    availability = Column(Boolean, nullable = False)   
    
    # v_02 argue code coulmn conatian information about floor number
    # 
    # v_01 suggestion  
    # hight discribes floor number
    # hieght = Column(Integer ,nullable = False)



    # building containing this floor
    building_id = Column(Integer , ForeignKey('building.id'))
    building = relationship(Building)


class Location(Base):
    '''
    Space/location Type: - maintains the faculty location/halls via storing the following information: 
        ✓ Id: Sequential number i.e. 1,2,3…  
        ✓ Code: - unique string that identifies the location i.e. LAB … 
        ✓ Description: - string describes the location i.e. Computer Lab  
        ✓ Color: - code that discriminate that space among other spaces. 
    # added
    * availability:  for inicating if location is functioning 
    ?? do we need this
    * regular_capacity: location capacity during regular days for better locating
    * exam_capacity: location capacity at exam time ( location can hold less at exam )
    ## relations

    Floor: floor_id whitch one contain this location
    ?? confirmation
    component_location:
    component: what available component for location EX:AC/board ..
    
    location_subject:
    subjects: associate subject to location ((* note period is defined 
                                                in subject no need for it in relation))
    
    ??confirmation ? does role describe which location user can edit/add
    role_locations
    role: roles which give permesion to view or edit in location 

    '''
    __tablename__ ='location'

    id = Column(Integer, primary_key=True)
    code = Column(String(250), nullable=False)
    description =Column(String(150), nullable = False)
    availability = Column(Boolean, nullable = False)

    color = Column(Integer, nullable = False)

    # capacity: location capacity during regular days for better locating
    # exam_capacity: location capacity at exam time ( location can hold less at exam )
    regular_capacity = Column(Integer) 
    exam_capacity = Column(Integer )
    
    # v_02 moved to seprate table named component
    # 
    # # v_01 added from 3.1.2 in SRS
    # datashow = Column(Boolean )
    # aircondition = Column(Boolean )
    # board = Column(Boolean)

    # floor containing this location
    floor_id = Column(Integer , ForeignKey('floor.id'))
    floor = relationship(Floor)


    roles = relationship(
        "Role",
        secondary='role_locations',
        back_populates="locations")

    compnents = relationship("Component",
        secondary='component_location',
        back_populates="locations")


    subjects = relationship("Subject",
                            secondary='location_subject',
                            back_populates="location")

# added table for component of lcation for making it more dynamic

class Component(Base):
    '''
    > confirm  __

    (*new generated) discribes component can be added to location :
        * id unique number for each component
        * name component name EX: AC / board ...

        #relation:
        # loction: locations has this component  many to many relation   
    '''
    __tablename__ = 'component'
    id = Column(Integer, primary_key=True)
    name =Column(String(150), nullable = False)
    locations = relationship("Location",
                            secondary='component_location',
                            back_populates="compnents")

# many to many relation between locations and components
component_location =Table('component_location' ,Base.metadata,
                Column('component_id' , Integer , ForeignKey('component.id')),
                Column('location_id', Integer, ForeignKey('location.id'))
                )



# 
class Department(Base):
    '''
     Departments: - maintains the following information for the department: - 
        ✓ Id: Sequential number i.e. 1,2,3…  
        ✓ Code: - unique string that identifies the department i.e. CVL, ELEC … 
        ✓ Name: - Department name i.e. architectural Engineering 
        ✓ Home Building: - the department’s home building which is to be selected from list of buildings (Screen A section 3.1.1). 

    # relations
    location_id : location holds this department
    ?? created relation was one to one do way need many building for same department 
    ?? or can two departement share same location
    '''
    __tablename__ ='department'

    id = Column(Integer, primary_key=True)
    code = Column(String(250), nullable=False)
    name =Column(String(150), nullable = False)

    # department building
    building_id = Column(Integer , ForeignKey('building.id'))
    building = relationship(Building)
   

class Staff(Base):
    '''
    Staff: - enables the user to add staff with the following data set: - 
        ✓ Id: Sequential number i.e. 1,2,3…  
        ✓ Name: - Staff member’s name. 
        ✓ Department: - staff member department which is to be selected from 
                        list of departments (Screen D section 3.1.1). 
        ✓ Position: - one position would be selected from a dropdown list contains  
                    the valid positions typically: 
                    ▪ Professor 
                    ▪ Associate Professor 
                    ▪ Assistant Professor 
                    ▪ Assistant lecturer 
                    ▪ Demonstrator 

    ?? is staff users for system who can login for viewing there data or it is public accessed
    '''
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    position = Column(String(10))

    department_id = Column(Integer , ForeignKey('department.id'))
    department = relationship(Department)
   
class Subject(Base):
    '''
     Subjects: - enables the user to add courses with the following data set: - 
     ✓ Id: Sequential number i.e. 1,2,3…  
     ✓ Code: - course code. 
     ✓ Name: - Subject name. 
     ✓ Lecture Time: - lecture time slot in Hours unit i.e. 1,2,3  ?? what does it mean in houres
     ✓ Department: - staff member department which is to be selected from list of departments (Screen D section 3.1.1). 
     ✓ preferred location type: one or many types would be selected from the list defined in subsection 3.1.1.C. i.e. CCE-108 course needs computer Lab so that we need to define such information right here. 
    
    # ?abdo ragab slot when lecture will be heled 
    # ?abdo ragab subject may share many departments why one-many relation    
    '''
    __tablename__ = 'subject'
    id= Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(50))
    # ?abdo ragab slot when lecture will be heled 
    lecture_time = Column(Integer)

    # ?abdo ragab subject may share many departments why one-many relation
    department_id = Column(Integer , ForeignKey('department.id'))
    department = relationship(Department)

    # you me not care about this it is just for implementing curd with session
    # it is not important for database creation in whole script 
    location = relationship(
                        "Location",
                        secondary='location_subject',
                        back_populates="subjects")

# table to relate location and subjects
location_subject = Table('location_subject', Base.metadata,
    Column('subject_id', Integer, ForeignKey('subject.id')),
    Column('location_id', Integer, ForeignKey('location.id'))
)    

class User(Base):
    '''
    B- Users: - this screen maintains users’ information in insert/update/delete 
                    manner with the following attributes: - 
    ✓ Id: serial 
    ✓ Name: user login name 
    ✓ Full name: user full name as four tokens first, middle, last and family name. 
    ✓ Email: to be used later to send required document to the user. 
    ✓ password 
    ✓ Role: - dropdown list to assign a role to the user.  
    '''
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    full_name = Column(String(150))
    email = Column(String(100))
    password = Column(String(30))
    role_id = Column(Integer , ForeignKey('role.id'))
    relationship('Role')

class Role(Base):
    '''
    A- Role: - this screen creates a role for user describing its job 
                i.e. admin, employee… 
    The screen maintains the following info. about the role: - 
    ✓ Id: Serial 
    ✓ Name: role name. 
    ✓ Description: role description.
    '''
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    Description = Column(String(200))
    locations = relationship(
        "Location",
        secondary='role_locations',
        back_populates="roles")



role_locations = Table('role_locations' , Base.metadata,
                Column('role_id' , Integer , ForeignKey('role.id')),
                Column('location_id', Integer, ForeignKey('location.id'))
                )

# to generate data base for sqlite (working)
engine = create_engine('sqlite:///lta01_oracle.db')
#  to generate for oracle
# engine = create_engine('oracle+cx_oracle://username:password@host:port/database')


Base.metadata.create_all(engine)

# # to generate erd from plantuml use 
# # http://www.plantuml.com
# 
# if __name__ == '__main__':
#     import codecs
#     import sadisplay

#     desc = sadisplay.describe(globals().values())

#     with codecs.open('schema.plantuml', 'w', encoding='utf-8') as f:
#         f.write(sadisplay.plantuml(desc))
