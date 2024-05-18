from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

class TeamMemberSetting(BoxLayout):
    text_input = StringProperty("")
    # player_name = ListProperty([])
    message_player = StringProperty("")
    message_team = StringProperty("")
    message_instruction = StringProperty("")

    def __init__(self, **kwargs):
        self.team_num = 0
        self.player_num = []
        self.player_name = []
        self.append_counter = 0
        self.team_pointer = 0
        super(TeamMemberSetting, self).__init__(**kwargs)
    
    def update_label(self, input):
        self.text_input = input
    
    def team_setting(self, team_num, player_num):
        self.team_num = team_num
        self.player_num = player_num
        for i in range(self.team_num):
            self.player_name.append([])
        self.message_team = f"Player num : {self.player_num}"
        # print(f"Team num : {self.team_num}\nPlayer num : {self.player_num}")
    
    def clear_input(self):
        self.text_input = ""

    def register(self):
        # Get team_pointer
        if self.team_pointer < self.team_num:
            if self.append_counter == self.player_num[self.team_pointer]:
                self.team_pointer += 1
                self.append_counter = 0
        
        # Add player
        if self.team_pointer < self.team_num:    
            self.player_name[self.team_pointer].append(self.text_input)
            self.append_counter += 1
            self.message_player = f"Added a player : {self.player_name}"
            if (self.team_pointer == self.team_num-1) and (self.append_counter == self.player_num[self.team_pointer]):
                self.message_instruction = "Go Next"
        else:
            pass

        
        self.clear_input()
    
    '''
    Check team setting
    '''
    def check_player_setting(self):
        check = True
        for i, team in enumerate(self.player_name):
            if len(team) == self.player_num[i]:
                pass
            else:
                check = False
        return check
        
class TeamMemberSettingApp(App):
    def build(self):
        return TeamMemberSetting()

if __name__ == "__main__":
    TeamMemberSettingApp().run()
