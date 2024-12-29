# Air Pollution Tracker

# Overview
Cron job application that will periodically fetch the current air quality (index and concentrations of pollutants) from the 
openweathermap API at specified latitude and longitude and then store pollution concentrations in a Redis database as time series data.

The time series data from Redis is then displayed in a dashboard using streamlit.

![Capture](https://github.com/user-attachments/assets/773a05d2-3684-45ed-950a-a6b57e967a0d)

## How to get started
1. Get API key from https://openweathermap.org/
2. create .env file in the root with variables LATITUDE, LONGITUDE, API_KEY, INTERVAL_IN_SECONDS
3. Run docker-compose build
4. Run docker-compose up
5. Navigate to http://localhost:8501/ to consult the dashboard.
6. Navigate to http://localhost:5540/ to use redis insight to explore Redis data.
