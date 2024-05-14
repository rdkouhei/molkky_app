from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '960')

from PointCalc import PointCalc
from MolkkyGameKivy import MolkkyGameKivy

class MainDisplay(BoxLayout):
    # Default Setting
    app_title = StringProperty("Molkky Scoreboard")
    input_text = StringProperty("Your Input")
    score_text = StringProperty("Your Score")

    player_point = StringProperty("")
    previous_point = StringProperty("12")
    pre_previous_point = StringProperty("6")
    
    team0_name = StringProperty("team0")
    team1_name = StringProperty("team1")

    team0_score = StringProperty("Score")
    team1_score = StringProperty("Score")

    team0_turn1 = StringProperty("")
    team0_turn2 = StringProperty("")
    team0_turn3 = StringProperty("")
    team0_turn4 = StringProperty("")
    team0_turn5 = StringProperty("")
    team0_turn6 = StringProperty("")
    team0_turn7 = StringProperty("")
    team0_turn8 = StringProperty("")
    team0_turn9 = StringProperty("")
    team0_turn10 = StringProperty("")
    team0_turn11 = StringProperty("")

    team0_points = [team0_turn1, team0_turn2, team0_turn3, team0_turn4, team0_turn5,
                    team0_turn6, team0_turn7, team0_turn8, team0_turn9, team0_turn10]

    team1_turn1 = StringProperty("")
    team1_turn2 = StringProperty("")
    team1_turn3 = StringProperty("")
    team1_turn4 = StringProperty("")
    team1_turn5 = StringProperty("")
    team1_turn6 = StringProperty("")
    team1_turn7 = StringProperty("")
    team1_turn8 = StringProperty("")
    team1_turn9 = StringProperty("")
    team1_turn10 = StringProperty("")
    team1_turn11 = StringProperty("")

    team1_points = [team1_turn1, team1_turn2, team1_turn3, team1_turn4, team1_turn5,
                    team1_turn6, team1_turn7, team1_turn8, team1_turn9, team1_turn10]

    title_fontsize = 55
    h1_fontsize = 40
    h2_fontsize = 32
    h3_fontsize = 24

    color_background = [0.66, 0.81, 0.93, 1]
    color_boader = [0.40, 0.65, 0.8, 0.3]

    member_list = [["jon", "van", "ken"],["tom", "xi", "luis"]]
    game_controller = MolkkyGameKivy(member_list)
    next_player_text = StringProperty("Team 0     " + game_controller.get_nextplayer(0))

    # team0_pointboard = ListProperty()
    # team0_pointboard = [StringProperty("10"), StringProperty("20")]

    def update_label(self, text):
        self.input_text = text

    def buttonClicked_back(self):
        self.input_text = 'Back'
    
    def buttonClicked_next(self):
        self.input_text = 'Next'
    
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

        


class MolkkyApp(App):
    def build(self):
        return MainDisplay()
    

if __name__ == '__main__':
    MolkkyApp().run()