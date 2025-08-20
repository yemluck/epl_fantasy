"""
1. create a class to store all 20 EPL teams
2. create a class for a player
3. create a method to pop any option the player picks in a game week
4. create a class which can take input by the admin for the week's score
4. run a compare function at the end of the game week
5. update each player's score

... room for more tasks
"""

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Player", "Points"]

#table.add_row(["Alice", 25,])

# Players list
# players = ["yemluck", "kay_uk", "tituswole", "exceptional", "khor", "sammy", "emrys", "feyishayur", "mr_harkin",
#            "ibidayo", "kay_man", "sk", "hazard10", "d", "hd", "kolarov"]
players = ["yemluck", "kay_uk", "tituswole"]

week_result = {
    "Arsenal": "",
    "Bournemouth": "",
    "Aston Villa": "",
    # "Brentford": "",
    # "Brighton": "",
    # "Burnley": "",
    # "Chelsea": "",
    # "Crystal Palace": "",
    # "Everton": "",
    # "Fulham": "",
    # "Leeds United": "",
    # "Liverpool": "",
    # "Man City": "",
    # "Man Utd": "",
    # "Newcastle United": "",
    # "Nottingham Forest": "",
    # "Sunderland": "",
    # "Tottenham": "",
    # "West Ham": "",
    # "Wolves": "",
}

class EplTeams:
    def __init__(self):
        self.teams = [
            "Arsenal",
            "Bournemouth",
            "Aston Villa",
            # "Brentford",
            # "Brighton",
            # "Burnley",
            # "Chelsea",
            # "Crystal Palace",
            # "Everton",
            # "Fulham",
            # "Leeds United",
            # "Liverpool",
            # "Man City",
            # "Man Utd",
            # "Newcastle United",
            # "Nottingham Forest",
            # "Sunderland",
            # "Tottenham",
            # "West Ham",
            # "Wolves"
        ]

class Player:
    # class to have player attribute like pick, score, position, options left
    def __init__(self, name):
        self.name = name
        self.pick = ""
        self.score = 0
        self.options = [
            "Arsenal",
            "Bournemouth",
            "Aston Villa",
            # "Brentford",
            # "Brighton",
            # "Burnley",
            # "Chelsea",
            # "Crystal Palace",
            # "Everton",
            # "Fulham",
            # "Leeds United",
            # "Liverpool",
            # "Man City",
            # "Man Utd",
            # "Newcastle United",
            # "Nottingham Forest",
            # "Sunderland",
            # "Tottenham",
            # "West Ham",
            # "Wolves"
        ]

# Create player instances
yemluck = Player("yemluck")
kay_uk = Player("kay_uk")
tituswole = Player("tituswole")
# exceptional = Player("exceptional")
# khor = Player("khor")
# sammy = Player("sammy")
# emrys = Player("emrys")
# feyishayur = Player("feyishayur")
# mr_harkin = Player("mr_harkin")
# ibidayo = Player("ibidayo")
# kay_man = Player("kay_man")
# sk = Player("sk")
# hazard10 = Player("hazard10")
# d = Player("d")
# hd = Player("hd")
# kolarov = Player("kolarov")

# Make a list of the players.
# player_list = [yemluck, kay_uk, tituswole, exceptional, khor, sammy, emrys, feyishayur, mr_harkin, ibidayo, kay_man,
#                sk, hazard10, d, hd, kolarov]

player_list = [yemluck, kay_uk, tituswole]
# start game
# update result
# each player picks a team

# Parameters to make the game rerun
game_week = 1

# Need to build a function to update the result dictionary
result_options = ["w", "d", "l"]

def update_result(result_dict):
    for team in result_dict:
        print(f"Gameweek {game_week}:")
        result_dict[team] = input(f"What was the result for {team}? (w/d/l): ").lower()
        if result_dict[team] not in result_options:
            print("Invalid result. Please try again.")
            result_dict[team] = input(f"What was the result for {team}? (w/d/l): ").lower()
    return result_dict

while game_week <=20:
    week_result = update_result(week_result)
    for player in player_list:
        print(player.options)
        player.pick = input(f"{player.name.title()}, make your pick for the week: ").title()
        if player.pick in player.options:
            if week_result[player.pick] == "w":
                player.score += 3
            elif week_result[player.pick] == "d":
                player.score += 1
            else:
                player.score += 0
            player.options.remove(player.pick)
        else:
            print("Invalid team name. Please try again.")
            player.pick = input(f"{player.name.title()}, make your pick for the week: ").title()

    for player in player_list:
        table.add_row([player.name.title(), player.score])

    game_week += 1
    print(table)
    print("\n" * 2)








