> ? > adding table for component/features of location

> ? does role describe which location user can edit/add

> ?? do we need many buildings for same department

> ?? can two departement share same building

> ?? are staff users for system who can login for viewing there data or it is public accessed

> ? what do you mean by houres unit in Lecture Time isn't they just slots

> ?subject may share many departments 
*( one department to many subject relation)

> ? does role describe which location user can edit/add


# Building: - maintains the faculty building via storing the following information: -   
    ✓ Id: Sequential number i.e. 1,2,3…  
    ✓ Code: - unique string that identifies the building i.e. A, B, C … 
    ✓ Description: - string describes the building i.e. Civil Eng Dept 


## added 
* availability for inicating if building is available as unavialble means you can't 
    add any thing to building locations 
<!-- > (abdo):?? no need for availability here location availability cover this  -->


# Building-Floor: - 
    maintains the faculty building floors via storing the following information:
    ✓ Id: Sequential number i.e. 1,2,3…
    ✓ Code: - unique string that identifies the sub-building i.e. A-1, A-2 …
    ✓ Description: - string describes the building i.e. 1st floor, 2nd floor 

## added
* availability for inicating if floor is available
?? no need for it location give this info
### relations
* building_id - floor has one to one relation with building 


# Space/location Type: - 
    maintains the faculty location/halls via storing the following information: 
    ✓ Id: Sequential number i.e. 1,2,3…  
    ✓ Code: - unique string that identifies the location i.e. LAB … 
    ✓ Description: - string describes the location i.e. Computer Lab  
    ✓ Color: - code that discriminate that space among other spaces. 
## added
* availability:  for inicating if location is functioning 
?? do we need this
* regular_capacity: location capacity during regular days for better locating
* exam_capacity: location capacity at exam time ( location can hold less at exam )

## relations

Floor: floor_id whitch one contain this location

> confirm  __

component_location:
component: what available component for location EX:AC/board ..

> confirm  __

location_subject:
subjects: associate subject to location ((* note slot is defined 
in subject no need for it in relation))

> confirm  __

role_locations
role: roles which give permesion to view or edit in location 
> ? does role describe which location user can edit/add

# component
> confirm  added

(*new generated) discribes component can be added to location :
* id :  unique number for each component
* name : component name i.e: AC / board ...
## relation:
 loction: locations has this component  
 type many to many relation   


# Departments: - 
    maintains the following information for the department: - 
    ✓ Id: Sequential number i.e. 1,2,3…  
    ✓ Code: - unique string that identifies the department i.e. CVL, ELEC … 
    ✓ Name: - Department name i.e. architectural Engineering 
    ✓ Home Building: - the department’s home building which is to be selected from list of buildings (Screen A section 3.1.1). 

# relations
location_id : location holds this department

> ?? do we need many building for same department 

> ?? can two departement share same building

# Staff: - 
    enables the user to add staff with the following data set: - 
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

> ?? is staff users for system who can login for viewing there data or it is public accessed


# Subjects: -
    enables the user to add courses with the following data set: - 
     ✓ Id: Sequential number i.e. 1,2,3…  
     ✓ Code: - course code. 
     ✓ Name: - Subject name. 
     ✓ Lecture Time: - lecture time slot in Hours unit i.e. 1,2,3  
     ✓ Department: - staff member department which is to be selected from list of departments (Screen D section 3.1.1). 
     ✓ preferred location type: one or many types would be selected from the list defined in subsection 3.1.1.C. i.e. CCE-108 course needs computer Lab so that we need to define such information right here. 

> ? what do you mean by houres unit in Lecture Time isn't they just slots

> ?subject may share many departments 
*( one department to many subject relation)





# Users: - 
no change

    this screen maintains users’ information in insert/update/delete 
    manner with the following attributes: - 
    ✓ Id: serial 
    ✓ Name: user login name 
    ✓ Full name: user full name as four tokens first, middle, last and family name. 
    ✓ Email: to be used later to send required document to the user. 
    ✓ password 
    ✓ Role: - dropdown list to assign a role to the user.  




# Role: - 
    this screen creates a role for user describing its job  i.e. admin,employee… 
    The screen maintains the following info. about the role: - 
    ✓ Id: Serial 
    ✓ Name: role name. 
    ✓ Description: role description.
> ? does role describe which location user can edit/add
