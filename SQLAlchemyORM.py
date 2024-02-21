from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sales.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key=True)

   name = Column(String)
   address = Column(String)
   email = Column(String)
Base.metadata.create_all(engine)

ORM1
>>> from sqlalchemy import create_engine
>>> engine = create_engine('sqlite:///college.db', echo = True)
engine = create_engine("mysql://user:pwd@localhost/college",echo = True)

dialect[+driver]://user:password@host/dbname


mysql+pymysql://<username>:<password>@<host>/<dbname>


1	
connect()

Returns connection object

2	
execute()

Executes a SQL statement construct

3	
begin()

Returns a context manager delivering a Connection with a Transaction established. Upon successful operation, the Transaction is committed, else it is rolled back

4	
dispose()

Disposes of the connection pool used by the Engine

5	
driver()

Driver name of the Dialect in use by the Engine

6	
table_names()

Returns a list of all table names available in the database

7	
transaction()

Executes the given function within a transaction boundary