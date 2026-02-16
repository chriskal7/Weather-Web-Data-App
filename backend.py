import requests

API_KEY = "6129d61ba1a8f3cb6901a7b41fd86edf" # Insert your api key, this has since been deleted.

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]

    return filtered_data

if __name__ == "__main__":
    print(get_data(place='Tokyo', forecast_days=3, kind="Temperature"))