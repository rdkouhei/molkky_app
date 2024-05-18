from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

class MainBoard(BoxLayout):

    def __init__(self, **kwargs):
        super(MainBoard, self).__init__(**kwargs)
    
class MainBoardApp(App):
    def build(self):
        return MainBoard()

if __name__ == "__main__":
    MainBoardApp().run()
