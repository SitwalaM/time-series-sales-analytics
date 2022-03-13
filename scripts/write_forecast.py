# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:33:59 2022

@author: user
"""

from write_db import update_db_with_data
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
#from pandas.io import sql
 

user = 'root'
passw = '****'
host =  'localhost'
port = 3306
database = 'salon_analytics'



database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(user, passw, 
                                                      host, database), pool_recycle=1, pool_timeout=57600).connect()

dataframe = pd.read_csv("full_forecast.csv") 


dataframe['ds']=pd.to_datetime(dataframe['ds'].astype(str))

dtypes_dictionary = {"ds": sqlalchemy.types.DateTime() ,
                   "yhat": sqlalchemy.types.Numeric,
                    "yhat_lower": sqlalchemy.types.Numeric,
                    "yhat_upper": sqlalchemy.types.Numeric,
                    "trend": sqlalchemy.types.Numeric       
                    }
   
update_db_with_data(database_connection, dataframe, "forecasts",  dtypes_dictionary)
