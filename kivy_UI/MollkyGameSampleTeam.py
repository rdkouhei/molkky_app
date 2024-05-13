from MolkkyGame import MolkkyGame
from PointCalc import PointCalc

class MolkkyGameSampleTeam(MolkkyGame):
    
    def __init__(self):
        self.team_list = [["jon", "van", "ken"],["tom", "xi", "luis"]]
        # super().__init__()
        self.teams = self.create_allteam()
    
    def create_singleteam(self, team_name, id):
        team_menber = self.team_list[id]

        team_setting = {
                        "team_name" : team_name,
                        "team_menber_num" : len(team_menber),
                        "team_member" : team_menber
                    }
        team = PointCalc(team_setting)
        return team
    
    def create_allteam(self):
        team_num = len(self.team_list) # todo : exeption
        teams = []
        
        # Create teams
        for i in range(team_num):
            team_name = "team" + str(i)
            teams.append(self.create_singleteam(team_name, i))

        for i, team in enumerate(teams):
            print(f"team{i}\n  {team.get_team_setting()}")

        return teams

# app = MolkkyGameSampleTeam()
# app.game_start()