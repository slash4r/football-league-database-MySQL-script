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

