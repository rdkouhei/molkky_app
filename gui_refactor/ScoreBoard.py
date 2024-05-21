from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty, ObjectProperty

from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '960')

# Import Original Module (../module/)
import sys
sys.path.append('../module/')
from PointCalc import PointCalc
from MolkkyGameKivy import MolkkyGameKivy
from TeamNumSetting import TeamNumSetting
from TeamMemberSetting import TeamMemberSetting

# kvファイルを画面ごとに分離してバラで読み込む
from kivy.lang import Builder
Builder.load_file('scoreboard.kv')
Builder.load_file('teamnumsetting.kv')
Builder.load_file('teammembersetting.kv')
from kivy.factory import Factory

class ScoreBoard(BoxLayout):
    '''
    Label Setting
    '''
    # Default Setting
    app_title = StringProperty("Molkky Scoreboard")
    input_text = StringProperty("Your Input")
    score_text = StringProperty("Your Score")

    player_point = StringProperty("")
    previous_point = StringProperty("")
    pre_previous_point = StringProperty("")   
    next_player_text = StringProperty("")
    go_next_screen = ObjectProperty(None)
 
    '''
    Team Property
    '''
    # Team0
    team0_name = StringProperty("team0")
    team0_score = StringProperty("Score")
    team0_points = ListProperty(['', '', '', '', '', '', '', '', '', '', 
                                 '', '', '', '', '', '', '', '', '', '',
                                 '', '', '', '', '', '', '', '', '', ''])
    # Team1
    team1_name = StringProperty("team1")
    team1_score = StringProperty("Score")
    team1_points = ListProperty(['', '', '', '', '', '', '', '', '', '', 
                                 '', '', '', '', '', '', '', '', '', '',
                                 '', '', '', '', '', '', '', '', '', ''])
    
    # Team2
    team2_name = StringProperty("team2")
    team2_score = StringProperty("Score")
    team2_points = ListProperty(['', '', '', '', '', '', '', '', '', '', 
                                 '', '', '', '', '', '', '', '', '', '',
                                 '', '', '', '', '', '', '', '', '', ''])
    
    # Team3
    team3_name = StringProperty("team3")
    team3_score = StringProperty("Score")
    team3_points = ListProperty(['', '', '', '', '', '', '', '', '', '', 
                                 '', '', '', '', '', '', '', '', '', '',
                                 '', '', '', '', '', '', '', '', '', ''])

    '''
    Graphical Property
    '''
    # Font Size
    title_fontsize = 55
    h1_fontsize = 40
    h2_fontsize = 32
    h3_fontsize = 24
    # Color
    color_background = [0.66, 0.81, 0.93, 1]
    color_boader = [0.40, 0.65, 0.8, 0.3]

    '''
    Method
    '''
    def __init__(self, **kwargs):
        self.clear_widgets()

        self.team0_score = "0"
        self.team1_score = "0"        
        self.team2_score = "0"        
        self.team3_score = "0"

        self.team0_points = ['', '', '', '', '', '', '', '', '', '', 
                            '', '', '', '', '', '', '', '', '', '',
                            '', '', '', '', '', '', '', '', '', '']
        self.team1_points = ['', '', '', '', '', '', '', '', '', '', 
                            '', '', '', '', '', '', '', '', '', '',
                            '', '', '', '', '', '', '', '', '', '']
        self.team2_points = ['', '', '', '', '', '', '', '', '', '', 
                            '', '', '', '', '', '', '', '', '', '',
                            '', '', '', '', '', '', '', '', '', '']
        self.team3_points = ['', '', '', '', '', '', '', '', '', '', 
                            '', '', '', '', '', '', '', '', '', '',
                            '', '', '', '', '', '', '', '', '', '']

        super(ScoreBoard, self).__init__(**kwargs)

    def reset_game(self, member):
        self.__init__()
        print(f"Score Board is loaded! Member {member}")
        self.member_list = member
        self.game_controller = MolkkyGameKivy(member)
        self.next_player_text = "Team 0       " + self.game_controller.get_nextplayer(0)
        
        # Team Oder ex) 3 teams : [1,2,0]
        self.team_oder = []
        for i in range(len(member)):
            if i != len(member)-1:
                self.team_oder.append(i+1)
            else:
                self.team_oder.append(0)

        self.add_round_widgets(len(self.team0_points))
        self.add_score_widget(len(member))
    
    def add_round_widgets(self, round_num):
        self.ids.grid_layout.cols = len(self.member_list) + 1 
        for i in range(round_num):
            self.add_round_label(i)
            self.add_round_button(i, len(self.member_list))

    def add_round_label(self,i):
        new_label = Label(text=str(i+1))
        self.ids.grid_layout.add_widget(new_label)
    
    def add_round_button(self, row, button_col):
        # 3チーム以上に対応させる
        bind_func = [self.bind_team0_point, self.bind_team1_point, self.bind_team2_point, self.bind_team3_point]
        team_points = [self.team0_points, self.team1_points, self.team2_points, self.team3_points]
        for i in range(button_col):
            new_button = Button()
            new_button.text = team_points[i][row]
            self.ids.grid_layout.add_widget(new_button)
            bind_func[i](new_button, row)

    def bind_team0_point(self, button, index):
        self.bind(team0_points=lambda instance, value: setattr(button, 'text', value[index]))
    
    def bind_team1_point(self, button, index):
        self.bind(team1_points=lambda instance, value: setattr(button, 'text', value[index]))
    
    def bind_team2_point(self, button, index):
        self.bind(team2_points=lambda instance, value: setattr(button, 'text', value[index]))
    
    def bind_team3_point(self, button, index):
        self.bind(team3_points=lambda instance, value: setattr(button, 'text', value[index]))

    def add_score_widget(self, team_num):
        score_board = self.ids.score_board
        score_board.clear_widgets()

        add_team_score_widget = [self.add_team0_score_widget, self.add_team1_score_widget, 
                                 self.add_team2_score_widget, self.add_team3_score_widget]
        for i in range(team_num):
            score_layout = add_team_score_widget[i]()
            score_board.add_widget(score_layout)

    def add_team0_score_widget(self):
        # Team 0 layout
        team0_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        team0_name_label = Factory.BorderLabel(text=self.team0_name, size_hint=(0.5, 0.3))
        team0_score_label = Factory.BorderLabel(text=self.team0_score, size_hint=(1, 0.7), font_size=48)
        team0_layout.add_widget(team0_name_label)
        team0_layout.add_widget(team0_score_label)
        self.bind(team0_score=lambda instance, value: setattr(team0_score_label, 'text', value))

        return team0_layout
    
    def add_team1_score_widget(self):
        # Team 1 layout
        team1_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        team1_name_label = Factory.BorderLabel(text=self.team1_name, size_hint=(0.5, 0.3))
        team1_score_label = Factory.BorderLabel(text=self.team1_score, size_hint=(1, 0.7), font_size=48)
        team1_layout.add_widget(team1_name_label)
        team1_layout.add_widget(team1_score_label)
        self.bind(team1_score=lambda instance, value: setattr(team1_score_label, 'text', value))

        return team1_layout
    
    def add_team2_score_widget(self):
        # Team 2 layout
        team2_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        team2_name_label = Factory.BorderLabel(text=self.team2_name, size_hint=(0.5, 0.3))
        team2_score_label = Factory.BorderLabel(text=self.team2_score, size_hint=(1, 0.7), font_size=48)
        team2_layout.add_widget(team2_name_label)
        team2_layout.add_widget(team2_score_label)
        self.bind(team2_score=lambda instance, value: setattr(team2_score_label, 'text', value))

        return team2_layout
    
    def add_team3_score_widget(self):
        # Team 3 layout
        team3_layout = BoxLayout(orientation='vertical', size_hint=(1, 1))
        team3_name_label = Factory.BorderLabel(text=self.team3_name, size_hint=(0.5, 0.3))
        team3_score_label = Factory.BorderLabel(text=self.team3_score, size_hint=(1, 0.7), font_size=48)
        team3_layout.add_widget(team3_name_label)
        team3_layout.add_widget(team3_score_label)
        self.bind(team3_score=lambda instance, value: setattr(team3_score_label, 'text', value))

        return team3_layout

    def next_game(self):
        self.reset_game(self.member_list)

    def update_label(self, text):
        self.input_text = text

    def add_number(self, number):
        self.player_point += number
    
    def clear_display(self):
        self.player_point = ""
    
    def register(self):
        if(self.player_point != ""):
            score, team_id, round = self.game_controller.add(int(self.player_point))
            next_team_id = self.team_oder[team_id]
            if(team_id == 0):
                self.team0_score = str(score)
                self.team0_points[round-1] = self.player_point
                self.next_player_text = f"Team {next_team_id}       " + self.game_controller.get_nextplayer(next_team_id)
            elif(team_id == 1):
                self.team1_score = str(score)
                self.team1_points[round-1] = self.player_point
                self.next_player_text = f"Team {next_team_id}       " + self.game_controller.get_nextplayer(next_team_id)
            elif(team_id == 2):
                self.team2_score = str(score)
                self.team2_points[round-1] = self.player_point
                self.next_player_text = f"Team {next_team_id}       " + self.game_controller.get_nextplayer(next_team_id)
            elif(team_id == 3):
                self.team3_score = str(score)
                self.team3_points[round-1] = self.player_point
                self.next_player_text = f"Team {next_team_id}       " + self.game_controller.get_nextplayer(next_team_id)
            self.clear_display()
        else:
            pass       

class ScoreBoardApp(App):
    def build(self):
        return ScoreBoard()

if __name__ == '__main__':
    ScoreBoardApp().run()