from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

import sys
sys.path.append('../module/')
from PointCalc import PointCalc
from MolkkyGameKivy import MolkkyGameKivy
from TeamNumSetting import TeamNumSetting
from TeamMemberSetting import TeamMemberSetting
from ScoreBoard import ScoreBoard

'''
Screen Class
'''
class ScreenTeamNumSetting(Screen):
    def __init__(self, **kwargs):
        super(ScreenTeamNumSetting, self).__init__(**kwargs)
        self.team_number_setting = TeamNumSetting()
        self.team_number_setting.go_next_screen = self.go_next_screen
        self.add_widget(self.team_number_setting)

    def go_next_screen(self):
        if self.team_number_setting.check_team_setting():
            # Pass team setting to new widget
            team_num = self.team_number_setting.team_num
            player_num = self.team_number_setting.player_num
            # self.member_setting_window.team_setting(team_num, player_num)

            next_screen = self.manager.get_screen('team_member_setting')
            next_screen.update_team_property(team_num, player_num)
            # Change Widget
            self.manager.current = 'team_member_setting'
        else:
            self.team_number_setting.message = "Team Setting is not completed."

class ScreenTeamMemberSetting(Screen):
    def __init__(self, **kwargs):
        super(ScreenTeamMemberSetting, self).__init__(**kwargs)
        self.member_setting = TeamMemberSetting()
        self.member_setting.go_next_screen = self.go_next_screen
        self.add_widget(self.member_setting)
    
    def update_team_property(self, team_num, player_num):
        self.member_setting.team_setting(team_num, player_num)

    def go_next_screen(self):
        if self.member_setting.check_player_setting():
            member_list = self.member_setting.player_name
            next_screen = self.manager.get_screen('score_board')
            next_screen.reset_game(member_list)
            # next_screen.member_list = member_list
            # next_screen.__init__()
            self.manager.current = 'score_board'
        else:
            self.member_setting.message_instruction = "Member Setting is not completed."

class ScreenScoreBoard(Screen):
    def __init__(self, **kwargs):
        super(ScreenScoreBoard, self).__init__(**kwargs)
        self.score_board = ScoreBoard()
        self.score_board.go_next_screen = self.go_next_screen
        self.add_widget(self.score_board)

    def reset_game(self, member_list):
        self.score_board.reset_game(member_list)

    def go_next_screen(self):
        self.manager.current = 'team_num_setting'

'''
Screen Manager Class
'''
class MyScreenManager(ScreenManager):
    pass

class MollkyScoreApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(ScreenTeamNumSetting(name='team_num_setting'))
        sm.add_widget(ScreenTeamMemberSetting(name='team_member_setting'))
        sm.add_widget(ScreenScoreBoard(name='score_board'))
        return sm

if __name__ == '__main__':
    MollkyScoreApp().run()