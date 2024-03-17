import random
import structure_lists

leagues = structure_lists.leagues_data
teams = structure_lists.teams_data
players = structure_lists.players_data
seasons = structure_lists.seasons


# def set_team_player_table(result_list: list) -> list:
#     player_id = 1
#     for i in range(0, 32):
#         for j in range(0, 5):
#             print(f"{teams[i][0]}  <->  {players[i][j][0]}")
#             print(f"team_id-{i+1}, player_id-{j+1}")
#             print()
#             result_list.append((i + 1, player_id))
#             player_id += 1
#     return result_list
#
#
# team_player_data = []
# set_team_player_table(team_player_data)
#
# print(team_player_data)
# print(len(teams))
# print(len(players))


def generate_leagues_inserts() -> str:
    result = "INSERT INTO Leagues (name, num_teams, country) VALUES\n"
    for i in range(0, len(leagues)):
        result += f"{leagues[i]},\n"
    result = result[:-2] + ";\n"
    return result


# print(generate_leagues_inserts())


def generate_teams_inserts() -> str:
    result = "INSERT INTO Teams (name, city, stadium, manager, league_id) VALUES\n"
    for i in range(0, len(teams)):
        result += f"{teams[i]},\n"
    result = result[:-2] + ";\n"
    return result


# print(generate_teams_inserts())


def generate_players_inserts() -> str:
    result = "INSERT INTO Players (name, birthday, nationality, position, number) VALUES\n"
    for i in range(0, len(teams)):
        for j in range(0, len(teams[i])):
            result += f"{players[i][j]},\n"
    result = result[:-2] + ";\n"
    return result


# print(generate_players_inserts())


def generate_team_player_inserts() -> str:
    result = "INSERT INTO Team_Player (team_id, player_id) VALUES\n"
    for i in range(1, len(teams)):
        for j in range(1, len(players[1]) + 1):
            result += f"({i + 1}, {j + i * 5}), "
        result += "\n"
    result = result[:-3] + ";\n"
    return result


# print(generate_team_player_inserts())


def generate_seasons_inserts() -> str:
    result = "INSERT INTO seasons (name) VALUES\n"
    for i in range(0, len(seasons)):
        result += f"('{seasons[i]}'), "
    result = result[:-2] + ";\n"
    return result


# print(generate_seasons_inserts())


def __new_match_day(season_id, league_id):
    result = ""
    used_days = set()
    counter = 0
    while counter != 8:
        match_day = random.randint(1, 365)
        while match_day in used_days:
            match_day = random.randint(1, 365)
        used_days.add(match_day)
        result += f"({season_id}, {league_id}, {match_day}), "
        counter += 1
    return result[:-1]


# print(__new_match_day(1, 1))


def generate_match_days_inserts():
    result = "INSERT INTO Match_days (season_id, league_id, day_number) VALUES\n"
    for s in range(1, len(seasons) + 1):
        for l in range(1, len(leagues) + 1):
            result += __new_match_day(s, l) + "\n"
    return result[:-2] + ";\n"


# print(generate_match_days_inserts())


def __random_time():
    start_hour = 13
    end_hour = 16

    hour = random.randint(start_hour, end_hour)
    minute = random.choice([15, 30, 45])

    time_string = f"{hour}:{minute:02d}:00"
    return time_string


def __get_teams_for_league(league_id, teams_data: list):
    return [team for team in teams_data if team[-1] == league_id]


def __days_to_month_day(days):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = 1
    day = days

    for i, days_in_current_month in enumerate(days_in_month):
        if day <= days_in_current_month:
            month = i + 1
            break
        day -= days_in_current_month

    return month, day


def generate_matches_and_goals_inserts():
    result1 = ("INSERT INTO Matches (venue, home_team_id, away_team_id, home_score, away_score, "
               "match_day_id) VALUES\n")
    result2 = "INSERT INTO Goals (match_id, player_id, team_id, time) VALUES\n"
    for s in seasons:
        for l in range(1, len(leagues) + 1):
            current_teams = __get_teams_for_league(l, teams)
            matches = set()
            while len(matches) < 8 and len(matches) < len(current_teams) * (len(current_teams) - 1):
                home_team, away_team = random.sample(current_teams, 2)
                if (home_team, away_team) not in matches:
                    matches.add((home_team, away_team))
                    stadium = home_team[2]

                    home_id = teams.index(home_team) + 1
                    away_id = teams.index(away_team) + 1

                    home_score = random.randint(0, 5)
                    away_score = random.randint(0, 5)

                    match_days_for_one_league = 8
                    season_id = seasons.index(s)
                    matches_for_one_season = match_days_for_one_league * len(leagues)

                    day_id = len(matches) + match_days_for_one_league * (l - 1) + matches_for_one_season * season_id
                    result1 += f"('{stadium}', '{home_id}', '{away_id}', '{home_score}', '{away_score}', '{day_id}'),\n"

                    while home_score != 0:
                        player_id = (home_id - 1) * len(home_team) + random.randint(1, 5)
                        result2 += f"('{day_id}', '{player_id}', '{home_id}', '{__random_time()}'), \n"
                        home_score -= 1

                    while away_score != 0:
                        player_id = (away_id - 1) * len(away_team) + random.randint(1, 5)
                        result2 += f"('{day_id}', '{player_id}', '{away_id}', '{__random_time()}'), \n"
                        away_score -= 1
    return result1[:-2] + ";\n", result2[:-3] + ";\n"

