import os
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

class Dialog1(FloatLayout):
    select = ObjectProperty(None)
    cancel = ObjectProperty(None)

class ConfirmPopup(BoxLayout):
    go_next = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ConfirmPopup, self).__init__(**kwargs)

    def on_button1_press(self):
        content = Dialog1(
            select=self.select,
            cancel=self.dismiss_popup)
        self._popup = Popup(title="Setting", content=content,
                            size_hint=(0.6, 0.3))
        self._popup.open()
        pass

    def select(self):
        self.go_next()
        self._popup.dismiss()
        pass

    def dismiss_popup(self):
        self._popup.dismiss()
        pass

class ConfirmPopupApp(App):
    def __init__(self, **kwargs):
        super(ConfirmPopupApp, self).__init__(**kwargs)
        self.title = 'Popup Test'

    def build(self):
        return ConfirmPopup()

if __name__ == '__main__':
    app = ConfirmPopupApp()
    app.run()