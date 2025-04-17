from langchain.tools import Tool
from services.football_api import search_team_id, get_last_matches


def fetch_team_stats(team_name: str) -> str:
    """Combines search and match data into a single string output."""
    team_id = search_team_id(team_name)
    if not team_id:
        return f"Could not find team named '{team_name}'."

    matches = get_last_matches(team_id)

    if not matches:
        return f"No recent matches found for '{team_name}'."

    summary = f"Last {len(matches)} matches for {team_name}:\n"
    for match in matches:
        summary += (
            f"{match['date']}: {match['home_team']} vs {match['away_team']} "
            f"({match['score']}) - Winner: {match['winner']}\n"
        )
    return summary


# LangChain Tool
team_stats_tool = Tool(
    name="FetchTeamStats",
    func=fetch_team_stats,
    description="Use this tool to get the last 5 games of a football team. Input should be the team name."
)