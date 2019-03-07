# script using 

edit line for with your user name and pass and database / or use sql lite no edit reqierd

```python
engine = create_engine('oracle+cx_oracle://username:password@host:port/database')
```

you may use other db provider to create your engine
https://docs.sqlalchemy.org/en/latest/core/engines.html


# further info about sqlalchemy and using it
https://docs.sqlalchemy.org/en/latest/orm/tutorial.html

# database using 
## setup enviroment 
* oracle database
* python3
### reqierd packages
* sql sqlalchemy -> use python object to create database
* cx_oracle -> db-api for oracle
* sadisplay -> create diagram for database
> pip3 install sqlalchemy cx_oracle sadisplay

