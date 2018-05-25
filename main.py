import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Contenedor_01(BoxLayout):
    None
class MainApp(App):
    title = "Hola Mundo"
    def build(self):
        return Contenedor_01()
if __name__ == '__main__':
    MainApp().run()