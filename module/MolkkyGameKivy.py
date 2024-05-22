from PointCalc import PointCalc

class MolkkyGameKivy():
    def __init__(self, team_list):
        self.team_list = team_list
        self.team_num  = len(self.team_list)
        self.teams = self.create_allteam()
        self.turn = 0
    
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
    
    '''
    UI >> Database
    '''
    def add(self, point):
        # if 
        turn_team_id = self.turn % self.team_num
        turn_team = self.teams[turn_team_id]
        score, is_continue = turn_team.add(point)
        round = turn_team.get_next_pointer()
        self.turn += 1
        proc_right = True
        return score, turn_team_id, round, proc_right

    # 点の修正用
    def add_middle(self, team_id, round, point):
        focus_team = self.teams[team_id]
        score, is_continue, ismiddle, proc_right = focus_team.add_middle(point, round)
        round += 1
        if ismiddle == False:
            self.turn += 1
            round = focus_team.get_next_pointer()
        return score, team_id, round, ismiddle, proc_right

    '''
    Database >> UI
    '''
    def get_nextplayer(self, team_id):
        return self.teams[team_id].next_player()
    
    def get_player(self, team_id, order):
        return self.teams[team_id].get_player(order)
    
    def get_point_board(self, team_id):
        point_board = self.teams[team_id].get_point_board()
        return point_board
    
    def get_score_board(self, team_id):
        score_board = self.teams[team_id].get_score_board()
        return score_board
    
    def get_team_setting(self, team_id):
        team_setting = self.teams[team_id].get_team_setting()
        return team_setting
    
    def get_score(self, team_id):
        score = self.teams[team_id].get_score()
        return score      
    
# menber_list = [["jon", "van", "ken"],["tom", "xi", "luis"]]
# app = MolkkyGameKivy(menber_list)
# # app.game_start()
# for i in range (10):
#     print("-----------------------------------")
#     print(app.get_nextplayer(0))
#     print(f"Add {i}")
#     print(app.add(i))

#     print(app.get_nextplayer(1))
#     print(f"Add {i+1}")
#     print(app.add(i+1))

#     print(app.get_score_board(0))
#     print(app.get_score_board(1))
