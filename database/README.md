[check changes](https://github.com/abdo1819/LTA/blob/master/database/change_log.md)

# intro
this is implemtaion of database for project using sqlalchemy witch support multi database provider

# using script

to create sqlite database 

> python3 database_setup.py

for other types
* edit this line with your info for oracle database
```python
engine = create_engine('oracle+cx_oracle://username:password@host:port/database')
```
* you may use other db provider 
### to create your engine
https://docs.sqlalchemy.org/en/latest/core/engines.html

## setup enviroment 
* oracle database
* python3
### reqierd packages
* sql sqlalchemy -> use python object to create database
* cx_oracle -> db-api for oracle
* sadisplay -> create diagram for database
> pip3 install sqlalchemy cx_oracle sadisplay

# further info about sqlalchemy and using it
https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
