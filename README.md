# Air Pollution Tracker

# Overview
Cron job application that will periodically fetch the air quality (index and concentrations of pollutants) from the 
openweathermap API.

## How to get started
1. Get API key from https://openweathermap.org/
2. create .env file in the root with variables LATITUDE, LONGITUDE, API_KEY, INTERVAL_IN_SECONDS
3. Run docker-compose build
4. Run docker-compose up