class PointCalc:
    
    '''
    Constructor
    '''
    def __init__(self, team_setting):
        self.team_setting = team_setting
        self.point_board = []
        self.score_board = []
        self.next_pointer = 0

    '''
    Score Manipulation
    '''
    def add(self, point):
        self.point_board.append([self.next_player(), point])
        score, is_continue = self.update_score()
        self.next_pointer += 1
        return score, is_continue
    
    def add_middle(self, point, num):
        if num < len(self.point_board):
            self.point_board[num][1] = point
            score, is_continue = self.update_score()
            ismiddle = True
            proc_right = True
        elif num == len(self.point_board):
            print(num)
            score, is_continue = self.add(point)
            ismiddle = False
            proc_right = True
        else:
            score = None
            is_continue = None
            ismiddle = None
            proc_right = False
        return score, is_continue, ismiddle, proc_right
    
    def back(self, num):
        self.point_board = self.point_board[:num]
        score, is_continue = self.update_score()
        self.next_pointer = num
        return score, is_continue
    
    def update_score(self):
        score = 0
        self.score_board = []
        for point in self.point_board:
            score += point[1]
            score, is_continue = self.check_score(score)
            self.score_board.append(score)
        return score, is_continue
    
    def next_player(self):
        return self.team_setting["team_member"][self.next_pointer % self.team_setting["team_menber_num"]]

    def check_score(self, score):
        if(score > 50):
            score = 25
            return score, True
        elif(score == 50):
            return score, False
        else:
            return score, True
    
    '''
    Get Function
    '''
    def get_team_setting(self):
        return self.team_setting
    
    def get_next_pointer(self):
        return self.next_pointer
    
    def get_point_board(self):
        return self.point_board
    
    def get_score_board(self):
        return self.score_board
            
    def get_score(self):
        return self.score_board[-1]
    
    def get_team_name(self):
        return self.team_setting["team_name"]
    
    def get_player(self, order):
        return self.team_setting["team_member"][order]