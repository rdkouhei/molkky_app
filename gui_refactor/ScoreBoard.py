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
    # team_num = StringProperty("")    
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

        # Reset variable
        self.team0_points = ['', '', '', '', '', '', '', '', '', '', 
                             '', '', '', '', '', '', '', '', '', '',
                             '', '', '', '', '', '', '', '', '', '']
        self.team1_points = ['', '', '', '', '', '', '', '', '', '', 
                             '', '', '', '', '', '', '', '', '', '',
                             '', '', '', '', '', '', '', '', '', '']
        self.team0_score = "0"
        self.team1_score = "0"        
        super(ScoreBoard, self).__init__(**kwargs)

        # self.ids.round1.text = "Hello"

    def reset_game(self, member):
        self.__init__()
        print(f"Score Board is loaded! Member {member}")
        self.member_list = member
        self.game_controller = MolkkyGameKivy(member)
        self.next_player_text = "Team 0       " + self.game_controller.get_nextplayer(0)
        self.add_round_widgets(len(self.team0_points))
    
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
        new_button_0 = Button()
        new_button_0.text = self.team0_points[row]
        self.ids.grid_layout.add_widget(new_button_0)
        self.bind_team0_point(new_button_0, row)

        new_button_1 = Button()
        new_button_1.text = self.team1_points[row]
        self.ids.grid_layout.add_widget(new_button_1)
        self.bind_team1_point(new_button_1, row)
    
    def bind_team0_point(self, button, index):
        self.bind(team0_points=lambda instance, value: setattr(button, 'text', value[index]))
    
    def bind_team1_point(self, button, index):
        self.bind(team1_points=lambda instance, value: setattr(button, 'text', value[index]))

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
            if(team_id == 0):
                self.team0_score = str(score)
                self.team0_points[round-1] = self.player_point
                self.next_player_text = "Team 1       " + self.game_controller.get_nextplayer(1)
            elif(team_id == 1):
                self.team1_score = str(score)
                self.team1_points[round-1] = self.player_point
                self.next_player_text = "Team 0       " + self.game_controller.get_nextplayer(0)
            self.clear_display()
        else:
            pass       

class ScoreBoardApp(App):
    def build(self):
        return ScoreBoard()

if __name__ == '__main__':
    ScoreBoardApp().run()