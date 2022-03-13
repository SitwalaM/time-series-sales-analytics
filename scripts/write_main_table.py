# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:33:48 2022

@author: SM
"""
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
#from pandas.io import sql
 

user = 'root'
passw = '******'  #insert your password here
host =  'localhost'
port = 3306
database = 'salon_analytics'


#read original customer data
customer_data = pd.read_csv("data.csv", decimal=".")
customer_data['Date']=pd.to_datetime(customer_data['Date'].astype(str))
customer_data = customer_data[customer_data['Date']> "2020-09-30"]

database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(user, passw, 
                                                      host, database), pool_recycle=1, pool_timeout=57600).connect()

customer_data.to_sql(con=database_connection, 
                     name='sales', 
                     if_exists='replace',
                     dtype = {"Date": sqlalchemy.types.DateTime() ,
                              "Customer": sqlalchemy.types.VARCHAR(length=255),
                              "Total": sqlalchemy.types.Numeric
                              },
                     chunksize=1000)

# wrap into function that can be usedin other scripts

def update_db_with_data(database_connection, dataframe, table_name, dtypes_dictionary):
    ''' function used to connect to update tables in the sql database
    inputs
    ------
    database_connection : connection object using sqlalchemy "create engine"
    dataframe: pandas datarame to be added to the database
    table_name: string name of table in database
    dtypes_dictionary: dictionary of datatypes for columns in the dataframe
    
    outputs
    -------
    None
    '''

    dataframe.to_sql(con=database_connection, 
                     name=table_name, 
                     if_exists='replace',
                     dtype = dtypes_dictionary,
                     chunksize=1000)
    return None

