import streamlit as st
import pandas as pd
from redis_client import get_redis_time_series_data

compounds = {
    "co": "Carbon Monoxide (CO)",
    "no": "Nitrogen monoxide (NO)",
    "no2": "Nitrogen dioxide (NO2)",
    "o3": "Ozone (O3)",
    "so2": "Sulfur dioxide (SO2)",
    "pm2_5": "Fine particles matter (PM2.5)",
    "pm10": "Coarse particulate matter (PM10)",
    "nh3": "Ammonia (NH3)",
}


def get_time_series_df(key):
    data = get_redis_time_series_data(key)
    df = pd.DataFrame(data, columns=["Timestamp", compounds[key]])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms', utc=True)
    df.set_index('Timestamp', inplace=True)
    return df


co_df = get_time_series_df("co")
no_df = get_time_series_df("no")
no2_df = get_time_series_df("no2")
o3_df = get_time_series_df("o3")
so2_df = get_time_series_df("so2")
pm2_5_df = get_time_series_df("pm2_5")
pm10_df = get_time_series_df("pm10")
nh3_df = get_time_series_df("nh3")

df_combined = co_df.join([no_df, no2_df, o3_df, so2_df, pm2_5_df, pm10_df, nh3_df], how='outer')

st.title("Air Pollution Tracker")
st.subheader(
    """Air pollution concentration tracker in µg/m³"""
)

st.line_chart(df_combined)

st.write(df_combined)
