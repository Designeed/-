from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.window import Window
Window.size = (412, 870)
Window.clearcolor = (.46, .15, .15, 1)

class LoginApp(App):
    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation = "vertical", size_hint = [None, None], size = [200, 300], spacing = 5)
        bl.add_widget(TextInput(text = "Логин", font_size = 32, background_color = [.18, .57, .39, 1]))
        bl.add_widget(TextInput(text = "Пароль", font_size = 32, background_color = [.18, .57, .39, 1]))
        bl.add_widget(Button(text = "Войти", font_size = 32, background_color = [.17, .84, .53, 1]))
        bl.add_widget(Button(text = "Регистрация", font_size = 32, background_color = [.17, .84, .53, 1], on_press = self.btn_press))
        bl.add_widget(MyCheckbox())
        bl.add_widget(Label(text = 'забыли пароль?', font_size = 16))
        al.add_widget(bl)
        return al

    def btn_press(self, instance):
        return 
        
            

        
class SScreem(Screen):
    def build(self):
        print("sdfsaf")
        
class MyCheckbox(GridLayout):
    def __init__(self):
        super().__init__()
        self.cols = 2
        self.add_widget(Label(text = 'запомнить пароль'))
        self.check = CheckBox(active = True)
        self.add_widget(self.check)

        
        
if __name__ == '__main__':    
    LoginApp().run()

    

