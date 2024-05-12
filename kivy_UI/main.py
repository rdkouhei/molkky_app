from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '960')

class MainDisplay(BoxLayout):
    app_title = StringProperty("Molkky Scoreboard")
    input_text = StringProperty("Your Input")
    score_text = StringProperty("Your Score")

    next_player_text = StringProperty("Team1 Kohei")
    player_point = StringProperty("")
    previous_point = StringProperty("12")
    pre_previous_point = StringProperty("6")
    
    team0_name = StringProperty("team0")
    team1_name = StringProperty("team1")

    team0_score = StringProperty("Score")
    team1_score = StringProperty("Score")

    h1_fontsize = 40
    h2_fontsize = 32
    h3_fontsize = 24

    color_background = [0.66, 0.81, 0.93, 1]
    color_boader = [0.40, 0.65, 0.8, 0.3]

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
        self.previous_point = self.player_point
        self.clear_display()


class MolkkyApp(App):
    def build(self):
        return MainDisplay()
    

if __name__ == '__main__':
    MolkkyApp().run()