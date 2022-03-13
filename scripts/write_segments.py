
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from write_db import update_db_with_data

 
user = 'root'
passw = '****' 
host =  'localhost'
port = 3306
database = 'salon_analytics'


database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(user, passw, 
                                                      host, database), pool_recycle=1, pool_timeout=57600).connect()

dataframe = pd.read_csv("segments.csv") 


dtypes_dictionary = {"dCustomer": sqlalchemy.types.String ,
                   "recency": sqlalchemy.types.Numeric,
                    "monetary": sqlalchemy.types.Numeric,
                    "frequency": sqlalchemy.types.Numeric,
                    "cluster": sqlalchemy.types.Numeric,
                    "segment": sqlalchemy.types.Numeric       
                    }
   
update_db_with_data(database_connection, dataframe, "segments",  dtypes_dictionary)

