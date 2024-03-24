import os
import time

from inserts_generators import *

colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}


def display_menu():
    print(colors["white"] + "Menu:")
    print("1. Generate Leagues Inserts")
    print("2. Generate Teams Inserts")
    print("3. Generate Players Inserts")
    print("4. Generate Team_Player Inserts")
    print("5. Generate Seasons Inserts")
    print("6. Generate Match_days Inserts")
    print("7. Generate Matches and Goals Inserts")
    print("8. Insert ALL!")
    print("9. Exit" + colors["reset"])


def write_to_file(filename, content):
    directory = "inserts_files"
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)


def generate_all_data():
    all_data = ""
    all_data += generate_leagues_inserts() + "\n\n"
    all_data += generate_teams_inserts() + "\n\n"
    all_data += generate_players_inserts() + "\n\n"
    all_data += generate_team_player_inserts() + "\n\n"
    all_data += generate_seasons_inserts() + "\n\n"
    all_data += generate_match_days_inserts() + "\n\n"
    matches_inserts, goals_inserts = generate_matches_and_goals_inserts()
    all_data += matches_inserts + "\n\n" + goals_inserts
    return all_data


def main():
    while True:
        display_menu()
        print(colors["red"] + "Be careful if you are generating inserts not for the first time. "
                              "It can OVERWRITE your previous results!")
        time.sleep(1)
        choice = input(colors["blue"] + "Enter what you want: " + colors["reset"])

        if choice == '1':
            write_to_file('leagues_inserts.sql', generate_leagues_inserts())
            print(colors["green"] + "Leagues inserts written to leagues_inserts.sql")
        elif choice == '2':
            write_to_file('teams_inserts.sql', generate_teams_inserts())
            print(colors["green"] + "Teams inserts written to teams_inserts.sql")
        elif choice == '3':
            write_to_file('players_inserts.sql', generate_players_inserts())
            print(colors["green"] + "Players inserts written to players_inserts.sql")
        elif choice == '4':
            write_to_file('team_player_inserts.sql', generate_team_player_inserts())
            print(colors["green"] + "Team Player inserts written to team_player_inserts.sql")
        elif choice == '5':
            write_to_file('seasons_inserts.sql', generate_seasons_inserts())
            print(colors["green"] + "Seasons inserts written to seasons_inserts.sql")
        elif choice == '6':
            write_to_file('match_days_inserts.sql', generate_match_days_inserts())
            print(colors["green"] + "Match Days inserts written to match_days_inserts.sql")
        elif choice == '7':
            matches_inserts, goals_inserts = generate_matches_and_goals_inserts()
            write_to_file('matches_inserts.sql', matches_inserts)
            write_to_file('goals_inserts.sql', goals_inserts)
            print(colors["green"] + "Matches inserts written to matches_inserts.sql")
            print(colors["green"] + "Goals inserts written to goals_inserts.sql")
        elif choice == '8':
            write_to_file('all_inserts.sql', generate_all_data())
            print(colors["green"] + "All data inserts written to all_inserts.sql")
        elif choice == '9':
            print(colors["red"] + "Exiting program...")
            time.sleep(1)
            break
        else:
            print(colors["red"] + "Invalid choice. Please try again." + colors["reset"])


if __name__ == "__main__":
    main()
