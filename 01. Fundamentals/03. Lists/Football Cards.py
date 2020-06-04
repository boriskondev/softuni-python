teams_and_cards = input().split()

team_a_rem = []
team_b_rem = []


for index in range(len(teams_and_cards)):
    team, player = teams_and_cards[index].split("-")
    if team == "A":
        if player not in team_a_rem:
            team_a_rem.append(player)
    elif team == "B":
        if player not in team_b_rem:
            team_b_rem.append(player)

print(f"Team A - {11 - len(team_a_rem)}; Team B - {11 - len(team_b_rem)}")
if len(team_a_rem) > 4 or len(team_b_rem) > 4:
    print("Game was terminated")