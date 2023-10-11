import requests
import time

# Define the URL you want to request
url = "https://crack3d-2023.onrender.com"

# Define the time interval in seconds (1 minute = 60 seconds)
interval = 60

while True:
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print(f"Request to {url} succeeded at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"Request to {url} failed with status code {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Wait for the specified interval before sending the next request
    time.sleep(interval)
