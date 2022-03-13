# Introduction

The project demonstrates basic time-series predictions and implementation of a dashboard using Tableau. The project was part of the [The Africa Data Science Intensive (DSI) program](http://dsi-program.com/). Softare used for this project;
* MySQL
* Python
* Tableau

# Files in Project
| File | Description |
|---|---|
| [salon_analytics_predictions.ipynb](https://github.com/SitwalaM/time-series-sales-analytics/blob/main/notebooks/salon_analytics_predictions.ipynb) |  Contains the time-series predictions using Prophet, xGBoost and LSTM|
| [customer_segmentation.ipynb](https://github.com/SitwalaM/time-series-sales-analytics/blob/main/notebooks/customer_segmentation.ipynb) | contains customer segmentation using RFM (Recency, Frequency and Monetary) |
| [write_main_table.py](https://github.com/SitwalaM/time-series-sales-analytics/blob/main/scripts/write_main_table.py)|Updates the main sql table "salon_analytics" to local database |
| [write_forecast.py](https://github.com/SitwalaM/time-series-sales-analytics/blob/main/scripts/write_forecast.py)|Updates the main sql table "forecasts" to local database |
| [write_segments.py](https://github.com/SitwalaM/time-series-sales-analytics/blob/main/scripts/write_segments.py) | Updates the main sql table "segments" to local database |

# Dataset
The project uses an anonymized dataset from a beauty shop in Lusaka, Zambia. The sale amounts (total) are also scaled to keep the business information private. dataset columns:

* **Date**: Hourly timestamp of customer purchases 
* **Customer**: Customer ID 
*  **Total**: Amount purchased.

The plot below shows the full plot of the dataset, it contains a timestamp of when each transaction was made.

![times-series](https://github.com/SitwalaM/time-series-sales-analytics/blob/main/images/time_plot.png)

# Loading dataset into MySQL Database

The data is loaded into a local MySQL database using python, after which Tableau is used to connect to the data for the dashboard. [sqlalchemy](https://www.sqlalchemy.org/) makes it easy to load data straight to MySQL databases. The following code shows an example of loading the main table to the database;

```Bash
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
 
#database credentials and details 
user = 'root'
passw = '******'  #insert your password here
host =  'localhost'
port = 3306
database = 'salon_analytics'

#read original customer data
customer_data = pd.read_csv("data.csv", decimal=".")
customer_data['Date']=pd.to_datetime(customer_data['Date'].astype(str))

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

```


# Time-Series Modelling

## Prophet

## xGBoost

## LSTM

# Customer Segmentation using RFM (Recency, Frequency, Monetary)

# License

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

# References
1. [YouTube Tableau Tutorial](https://www.youtube.com/watch?v=cmuJ0IhDo7o)

