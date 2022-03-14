# Introduction

The project demonstrates basic time-series predictions and implementation of a dashboard using Tableau. The project was part of the [The Africa Data Science Intensive (DSI) program](http://dsi-program.com/). Softare used for this project:
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

The data is loaded into a local MySQL database using python, after which Tableau is used to connect to the data for the dashboard. [sqlalchemy](https://www.sqlalchemy.org/) makes it easy to load data straight to MySQL databases. The following code shows an example of loading the main table to the database:

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

Forecast were performed using three models: [Prophet](https://facebook.github.io/prophet/), [xGBoost](https://xgboost.readthedocs.io/en/stable/) and [LSTM ](https://en.wikipedia.org/wiki/Long_short-term_memory). A forecast size of 7 days was used as the samplesize of the dataset is too small (15 months) for a mothly horizon.

## Prophet

Prophet(https://facebook.github.io/prophet/) is an open source procedure for fitting time-series. It decomposes the trend, seasonality and cyclic behaviour of a time-series. Our data in this case is highly seasonal at a weakly basis, the best days for sales are Sunday. The data also showed a sudden increase in trend due to change in Covid-19 restrictions. Further details and full code of the predictions can be found [in this notebook](https://github.com/SitwalaM/time-series-sales-analytics/blob/main/notebooks/salon_analytics_predictions.ipynb). The main components of the time-series Zambian holidays are shown below,

![decompose](https://github.com/SitwalaM/time-series-sales-analytics/blob/main/images/prophet_decompose.PNG)


### Modeling

The following parameters were used to fit the prophet model
```Bash
m = Prophet(interval_width=0.95, weekly_seasonality=False, 
            seasonality_mode = 'multiplicative', 
            holidays= zambia_holidays, 
            changepoint_range=0.8).add_seasonality(name="weekly", period= 7, fourier_order= 25)
m.fit(train)
```
The model can be improved by varying the change point range and manually adding the fourier order of the seasonality for your specific series. The parameters above improved the predictions.

### Prophet Results

|**mean absolute error MAE:**| 92.5 |
|---|---|
|**mean absolute percentage error MAPE:**| **0.5** |

![prophet_prediction](https://github.com/SitwalaM/time-series-sales-analytics/blob/main/images/prophet_with_conf.png)

## xGBoost

![ Extreme Gradient Boosting (xGBoost)](https://xgboost.readthedocs.io/en/stable/) is normally the go to algorithm for tabular data as it produces good results in short prediction times. 

### Modelling

For xGBoost, the days of the week were one-hot encoded as the sales are highly dependant on what day of the week it is. The one-hot encoding was done as follows before splitting the into training and testing set,

```Bash

# Add days of the week to the dataframe
grouped_day["day_of_week"] = grouped_day['Date'].dt.strftime("%A")

# add one hot encoding for the days
encodes = pd.get_dummies(grouped_day["day_of_week"])
grouped_day2 = pd.concat([encodes,grouped_day.drop("day_of_week", axis=1)], axis=1)

# The last column of the encoding can then be removed as it becomes redundant 
```
Full code and details of the training can be found in [this notebook](salon_analytics_predictions.ipynb).

### xGBoost Results

|**mean absolute error MAE:**| 117 |
|---|---|
|**mean absolute percentage error MAPE:**| **0.41** |

![xGBoost_Plot](https://github.com/SitwalaM/time-series-sales-analytics/blob/main/images/xgboost_pred.png)

## LSTM

# Customer Segmentation using RFM (Recency, Frequency, Monetary)

# License

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

# References
1. [YouTube Tableau Tutorial](https://www.youtube.com/watch?v=cmuJ0IhDo7o)

