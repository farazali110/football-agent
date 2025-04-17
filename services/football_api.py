import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FOOTBALL_API_KEY")
BASE_URL = "https://api.football-data.org/v4"

HEADERS = {
    "X-Auth-Token": API_KEY
}


def search_team_id(team_name):
    """Get team ID by fuzzy matching name (first match)."""
    url = f"{BASE_URL}/teams"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception("Failed to fetch teams.")
    
    all_teams = response.json().get("teams", [])
    for team in all_teams:
        if team_name.lower() in team["name"].lower():
            return team["id"]
    return None


def get_last_matches(team_id, limit=5):
    """Get last N finished matches for a given team ID."""
    url = f"{BASE_URL}/teams/{team_id}/matches?status=FINISHED&limit={limit}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception("Failed to fetch match data.")
    
    matches = response.json().get("matches", [])
    results = []
    for match in matches:
        result = {
            "date": match["utcDate"][:10],
            "competition": match["competition"]["name"],
            "home_team": match["homeTeam"]["name"],
            "away_team": match["awayTeam"]["name"],
            "score": f'{match["score"]["fullTime"]["home"]} - {match["score"]["fullTime"]["away"]}',
            "winner": match["score"]["winner"]
        }
        results.append(result)
    
    return results