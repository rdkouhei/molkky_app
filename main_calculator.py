# Calculate point (for single team)
class PointCalc:
    team_param = {}

    def __init__(self, team_param):
        self.team_param = team_param

# Create single team    
def create_team(num, team_menber):
    team_param = {"team_name" : "team"+str(num),
                  "team_member" : team_menber
                 }
    team = PointCalc(team_param)
    return team

def main():
    team_num = int(input("Enter number of teams  : "))
    teams = []
    
    # Create teams
    for i in range(team_num):
        # Create single team
        team_menber = []
        team_menber_num = int(input(f"Enter team{i} number of menber : "))
        for j in range(team_menber_num):
            team_menber.append(input(f"Enter team{i} menber{j} name : "))
            
        teams.append(create_team(i, team_menber))

    for i, team in enumerate(teams):
        print(f"team{i}\n  {team.team_param}")

    return 0

if __name__ == "__main__":
    main()