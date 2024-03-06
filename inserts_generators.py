import structure_lists

leagues = structure_lists.leagues_data
teams = structure_lists.teams_data
players = structure_lists.players_data


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
    for i in range(0, 8):
        result += f"{leagues[i]},\n"
    result = result[:-2] + ";\n"
    return result
print(generate_leagues_inserts())


def generate_teams_inserts() -> str:
    result = "INSERT INTO Teams (name, city, stadium, manager, league_id) VALUES\n"
    for i in range(0, 32):
        result += f"{teams[i]},\n"
    result = result[:-2] + ";\n"
    return result
print(generate_teams_inserts())


def generate_players_inserts() -> str:
    result = "INSERT INTO Players (name, birthday, nationality, position, number) VALUES\n"
    for i in range(0, 32):
        for j in range(0, 5):
            result += f"{players[i][j]},\n"
    result = result[:-2] + ";\n"
    return result
print(generate_players_inserts())


def generate_team_player_inserts() -> str:
    result = "INSERT INTO Team_Player (team_id, player_id) VALUES\n"
    for i in range(1, 33):
        for j in range(1, 6):
            result += f"({i}, {j + (i-1) * 5}), "
        result += "\n"
    result = result[:-3] + ";\n"
    return result
print(generate_team_player_inserts())
