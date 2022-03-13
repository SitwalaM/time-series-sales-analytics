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
The project uses an anonymized dataset from a beauty shop in Lusaka, Zambia. The sale amounts (total) are also scaled to protect the business. dataset columns:

* **Date**: Hourly timestamp of customer purchases 
* **Customer**: Customer ID 
*  **Total**: Amount purchased.

# Loading dataset into MySQL Database


# Time-Series Modelling

## Prophet

## xGBoost

## LSTM

# Customer Segmentation using RFM (Recency, Frequency, Monetary)

# License

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

# References
1. [YouTube Tableau Tutorial](https://www.youtube.com/watch?v=cmuJ0IhDo7o)

