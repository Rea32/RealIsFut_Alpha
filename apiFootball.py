import requests

# Define the API endpoint and your API key
url = "https://apiv3.apifootball.com/?action=get_countries"
# Define the API method and your API key
api_method = "get_countries"
api_key = "c9b052702f6a4870e497f31a2a2a4f1b3e0a9483dc8000986c53797bb7897787"  # Replace with your actual API key

liga_id = ""
# Define the query parameters as a dictionary
params = {
    "action": api_method,
    "APIkey": api_key
}

# Send a GET request to the API endpoint
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    for country in data:
        if country['country_name'] == "Europe":
            liga_id = country['country_id']
            print(liga_id) 
else:
    print("Error: Unable to retrieve data. Status code:", response.status_code)
