from datetime import datetime,timedelta
import requests

#-- OBTENER PAISES --
def getCountries():
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
    response= requests.get(url, params=params)
    countries = response.json()
    return {"response" : response,"countries" : countries}

#-- OBTENER COMPETICIONES (segun pais) --
def getCompetitions(pais):
    # Define the API endpoint and your API key
    url = "https://apiv3.apifootball.com/?action=get_leagues"
    # Define the API method and your API key
    api_method = "get_leagues"
    api_key = "c9b052702f6a4870e497f31a2a2a4f1b3e0a9483dc8000986c53797bb7897787"  # Replace with your actual API key

    liga_id = ""
    # Define the query parameters as a dictionary
    params = {
        "action": api_method,
        "APIkey": api_key,
        "country_id" : pais
    }
    # Send a GET request to the API endpoint
    response= requests.get(url, params=params)
    competitions = response.json()
    
    return {"response" : response,"competitions" : competitions}

#-- OBTENER EVENTOS (determinada liga y partidos) --
def getEvents(competicion = "", match = ""):
    # Define the API endpoint and your API key
    url = "https://apiv3.apifootball.com/?action=get_events"
    # Define the API method and your API key
    api_method = "get_events"
    api_key = "c9b052702f6a4870e497f31a2a2a4f1b3e0a9483dc8000986c53797bb7897787"  # Replace with your actual API key
    actual_date = datetime.now().strftime("%Y-%m-%d")
    liga_id = ""
    # Define the query parameters as a dictionary
    params = {
        "action": api_method,
        "APIkey": api_key,
        "league_id" : competicion,
        "from" : actual_date,
        "to" : actual_date
    }
    # Send a GET request to the API endpoint
    response = requests.get(url, params=params)
    events = response.json()
    return {"response" : response,"events" : events}

#-- OBTENER PARTIDO --
def getMatch(match):
    # Define the API endpoint and your API key
    url = "https://apiv3.apifootball.com/?action=get_events"
    # Define the API method and your API key
    api_method = "get_events"
    api_key = "c9b052702f6a4870e497f31a2a2a4f1b3e0a9483dc8000986c53797bb7897787"  # Replace with your actual API key
    actual_date = datetime.now().strftime("%Y-%m-%d")
    liga_id = ""
    # Define the query parameters as a dictionary
    params = {
        "action": api_method,
        "APIkey": api_key,
        "match_id" : match,
        "from" : actual_date,
        "to" : actual_date
    }
    # Send a GET request to the API endpoint
    response = requests.get(url, params=params)
    events = response.json()
    return {"response" : response,"events" : events}

#print(getMatch("208975"))
"""for key in getEvents(302)["events"][0].keys():

    print(key)"""
#print(getEvents(302)["events"][0]["match_live"])
"""for key in getCountries()["countries"][0].keys():

    print(key)
print(getCountries())"""

#-- OBTENER CARA A CARA --
def getHeadToHead(firstTeam,secondTeam):
    # Define the API endpoint and your API key
    url = "https://apiv3.apifootball.com/?action=get_H2H"
    # Define the API method and your API key
    api_method = "get_H2H"
    api_key = "c9b052702f6a4870e497f31a2a2a4f1b3e0a9483dc8000986c53797bb7897787"  # Replace with your actual API key

    # Define the query parameters as a dictionary
    params = {
        "action": api_method,
        "APIkey": api_key,
        "firstTeamId" : firstTeam,
        "secondTeamId" : secondTeam
    }
    # Send a GET request to the API endpoint
    response = requests.get(url, params=params)
    h2h = response.json()
    return {"response" : response,"h2h" : h2h}

#-- OBTENER EQUIPO --
def getTeam(team_id):
    # Define the API endpoint and your API key
    url = "https://apiv3.apifootball.com/?action=get_teams"
    # Define the API method and your API key
    api_method = "get_teams"
    api_key = "c9b052702f6a4870e497f31a2a2a4f1b3e0a9483dc8000986c53797bb7897787"  # Replace with your actual API key

    # Define the query parameters as a dictionary
    params = {
        "action": api_method,
        "APIkey": api_key,
        "team_id" : team_id,
    }
    response = requests.get(url, params=params)
    team = response.json()
    return {"response" : response,"team" : team}


