from PointCalc import PointCalc

class MolkkyGame:
    '''
    Constructor
    '''
    def __init__(self):
        self.teams = self.create_allteam()

    def create_singleteam(self, team_name):
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
    
    def create_allteam(self):
        team_num = int(input("Enter number of teams  : ")) # todo : exeption
        teams = []
        
        # Create teams
        for i in range(team_num):
            team_name = "team" + str(i)
            teams.append(self.create_singleteam(team_name))

        for i, team in enumerate(teams):
            print(f"team{i}\n  {team.get_team_setting()}")

        return teams
    
    def game_start(self):
        while(True):
            is_continue = None
            for team in self.teams:
                print(f"Next Player >> {team.get_team_name()} : {team.next_player()}")
                score, is_continue = team.add(int(input(f"Enter {team.next_player()} Point : "))) # todo : exeption
                print(f"{team.get_team_name()} Total Score : < {score} >")
                print(f"{team.get_team_name()} Point Board: < {team.get_point_board()} >")
                if(not is_continue):
                    print(f"Game finished! Winner is {team.get_team_name()}")
                    break
            if(not is_continue):
                break

# app = MolkkyGame()
# app.game_start()