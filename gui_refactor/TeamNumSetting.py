from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, ObjectProperty

from kivy.uix.screenmanager import Screen

from kivy.lang import Builder
# Builder.load_file('teammembersetting.kv')

class TeamNumSetting(BoxLayout):
    message = StringProperty("")
    setting_view = ListProperty([])
    user_input = StringProperty("")
    go_next_screen = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        self.message = "Input Team Number"
        self.register_func = [self.register_team_num, self.register_player_num]
        self.register_mode = 0
        self.register_player_num_count = 0
        self.setting_view = ["", ""]
        
        self.team_num = -1
        self.player_num = []
        
        super(TeamNumSetting, self).__init__(**kwargs)
    
    def add_number(self, number):
        print("add num called")
        self.user_input += number
    
    def clear_display(self):
        self.user_input = ""
    
    '''
    Register Property(Number of Team and Member)
    '''
    def register_team_num(self):
        if int(self.user_input) != 0:
            self.team_num = int(self.user_input)
            self.clear_display()
            self.setting_view[0] = f"Team Number : {self.team_num}"
            self.message = "Input Player Number"
            self.register_mode += 1
        else:
            self.message = "Incorrect Input(0)\nInput Team Number"
            self.clear_display()
                        
    def register_player_num(self):
        if int(self.user_input) != 0:
            self.player_num.append(int(self.user_input))
            self.clear_display()
            self.setting_view[1] += f"Team {self.register_player_num_count}, Player Number : {self.player_num[-1]}\n"
            self.register_player_num_count += 1
            if self.register_player_num_count >= self.team_num:
                self.message = "Go to Next"
                self.register_mode += 1
            else:
                self.message = "Input Player Number"
        else:
            self.message = "Incorrect Input(0)\nInput Player Number"

    def register(self):
        try:
            int(self.user_input)
        except ValueError:
            print("Input Integer Value")
        else:
            if self.register_mode < len(self.register_func):
                self.register_func[self.register_mode]()
            else:
                print("Go to Next")
    
    '''
    Check team setting
    '''
    def check_team_setting(self):
        return self.team_num == len(self.player_num)

class TeamNumSettingApp(App):
    def build(self):
        return TeamNumSetting()

if __name__ == "__main__":
    TeamNumSettingApp().run()
