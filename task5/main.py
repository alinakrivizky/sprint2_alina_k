import football
import hockey

football_team = football.Football(2, 2, 2)
hockey_team = hockey.Hockey(2, 2, 2)

football_methods = [
    football_team.number_of_wins,
    football_team.number_of_draws,
    football_team.number_of_losses,
    football_team.total_points
]

hockey_methods = [
    hockey_team.number_of_wins,
    hockey_team.number_of_draws,
    hockey_team.number_of_losses,
    hockey_team.total_points
]

for method in football_methods:
    print(method())
for method in hockey_methods:
    print(method())

