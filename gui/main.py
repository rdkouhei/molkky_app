from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

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
Builder.load_file('teamnumsetting.kv')
Builder.load_file('teammembersetting.kv')
from kivy.factory import Factory

class MainDisplay(BoxLayout):
    '''
    Game Setting
    '''
    member_list = [["jon", "van", "ken"],["tom", "xi", "luis"]] # Sample Team

    team_setting_window = None
    member_setting_window = None

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
 
    '''
    Team Property
    '''
    # Team0
    team0_name = StringProperty("team0")
    team0_score = StringProperty("Score")
    team0_points = ListProperty(['', '', '', '', '', '',
                                 '', '', '', '', ''])
    # Team1
    team1_name = StringProperty("team1")
    team1_score = StringProperty("Score")
    team1_points = ListProperty(['', '', '', '', '', '',
                                 '', '', '', '', ''])
    
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
        self.team_num_window = TeamNumSetting()
        self.member_setting_window = TeamMemberSetting()
        self.game_controller = MolkkyGameKivy(self.member_list)

        # Reset variable
        self.team0_points = ['', '', '', '', '', '',
                                 '', '', '', '', '']
        self.team1_points = ['', '', '', '', '', '',
                                 '', '', '', '', '']
        self.team0_score = "0"
        self.team1_score = "0"
        self.next_player_text = "Team 0       " + self.game_controller.get_nextplayer(0)
        
        super(MainDisplay, self).__init__(**kwargs)

    def update_label(self, text):
        self.input_text = text

    def buttonClicked_back(self):
        self.input_text = 'Back'
    
    def buttonClicked_next(self):
        # Change Widget
        self.clear_widgets()
        self.add_widget(self.team_num_window)
    
    # def buttonClicked_back(self):
    #     self.clear_widgets()
    #     self.add_widget(self.main_board)

    def buttonPlayerSetting(self):
        if self.team_num_window.check_team_setting():
            # Pass team setting to new widget
            team_num = self.team_num_window.team_num
            player_num = self.team_num_window.player_num
            self.member_setting_window.team_setting(team_num, player_num)

            # Change Widget
            self.clear_widgets()
            self.add_widget(self.member_setting_window)
        else:
            self.team_num_window.message = "Team Setting is not completed."
    
    def buttonStartGame(self):
        if self.member_setting_window.check_player_setting():
            self.member_list = self.member_setting_window.player_name
            self.clear_widgets()
            self.__init__()
        else:
            self.member_setting_window.message_instruction = "Member Setting is not completed."

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
    
    # def chage_window(self):
    #     self.clear_widgets()
    #     self.add_widget(self.setting_window)

    # def add_team_ok(self, number):
    #     self.team_num += number
        


class MolkkyApp(App):
    def build(self):
        return MainDisplay()
    

if __name__ == '__main__':
    MolkkyApp().run()