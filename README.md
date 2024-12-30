# Air Pollution Tracker

# Overview
Celery backend application, using Redis as a broker, that will periodically fetch the current air quality (index and concentrations of pollutants) from the 
openweathermap API at specified latitude and longitude. 

After fetching the pollution data, it is then stored as time series data in the same Redis instance used by Celery.

The time series data from Redis is then displayed in a Grafana dashboard using Prometheus as a data source.

## How to get started
1. Create account and get API key from https://openweathermap.org/ (verify email and there might be a short delay for API key to become active)
2. Create .env file in the root of the project with variables LATITUDE, LONGITUDE, API_KEY, INTERVAL_IN_SECONDS
```
LATITUDE=40.7128
LONGITUDE=-74.0060
API_KEY=<API KEY HERE>
INTERVAL_IN_SECONDS=10
```
3. Optionally you can add to .env file variables FROM_EMAIL, FROM_PASSWORD, TO_EMAIL to create email alerts for air quality index above 4 using smtp.gmail.com
4. 'Run docker-compose build' command in the root of the project
5. 'Run docker-compose up' command in the root of the project
6. Navigate to http://localhost:3000/ to consult the Grafana dashboard.
   - Username and password are 'admin'
   - Skip change password step
   - Navigate to Air Pollution Tracker under dashboards section
