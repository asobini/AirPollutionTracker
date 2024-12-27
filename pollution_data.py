import requests


def fetch_air_pollution_data(lat, lon, api_key):
    """
    Fetch air pollution data from the OpenWeatherMap API.

    Parameters:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        api_key (str): Your OpenWeatherMap API key.
    """
    url = f"http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        return extract_info_from_response(response.json())
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def extract_info_from_response(json):
    data = json["list"][0]
    return {
        "timestamp": data['dt'],
        "air_quality_index": data['main']['aqi'],
        "components": data['components'],
    }
