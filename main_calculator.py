from PointCalc import PointCalc

# Create Single Team    
def create_team(team_name):
    team_menber = []
    team_menber_num = int(input(f"Enter {team_name} number of menber : ")) # todo : exeption
    for i in range(team_menber_num):
        team_menber.append(input(f"Enter {team_name} menber{i} name : "))

    team_setting = {
                    "team_name" : team_name,
                    "team_menber_num" : len(team_menber),
                    "team_member" : team_menber
                   }
    team = PointCalc(team_setting)
    return team

# Team Setting
def game_setting():
    team_num = int(input("Enter number of teams  : ")) # todo : exeption
    teams = []
    
    # Create teams
    for i in range(team_num):
        team_name = "team" + str(i)
        teams.append(create_team(team_name))

    for i, team in enumerate(teams):
        print(f"team{i}\n  {team.get_team_setting()}")

    return teams

# Start Game Loop
def game_start(teams):
    while(True):
        is_continue = None
        for team in teams:
            print(f"Next Player >> {team.get_team_name()} : {team.next_player()}")
            score, is_continue = team.add(int(input(f"Enter {team.next_player()} Point : "))) # todo : exeption
            print(f"{team.get_team_name()} Total Score : < {score} >")
            print(f"{team.get_team_name()} Point Board: < {team.get_point_board()} >")
            if(not is_continue):
                print(f"Game finished! Winner is {team.get_team_name()}")
                break
        if(not is_continue):
            break
            
def main():
    '''
    Setting
    '''
    teams = game_setting()
    
    '''
    Game
    '''
    game_start(teams)

    '''
    Finish, Next game
    '''

    return 0

if __name__ == "__main__":
    main()