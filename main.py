from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

#importa classe da janela principal
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
Window.clearcolor = get_color_from_hex("#f8feff")
#forca a alicativo a nao iniciar em tela cheia

from kivy.config import Config
Config.set("graphics" , "fullscreen", "0")
Config.set("graphics" , "resizable", "0")
Window.size = 1350,650

class Janelas(BoxLayout):
    def Voltar(BoxLayout):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Inplementa())
        print("Voltar")

class SysApp(App):
    def build(self):
        return Inplementa()
    
class Inplementa(BoxLayout):

    def Relatorio(self):
        print("Relatorio")

    def Exibir(self):        
        print("Exibir!")

    def Editar(self):
        print("Editar")

    def Manuntecao(self):
        exit()

    def Configuracao(BoxLayout):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Janelas())
        print("configuracao")
   
janela = SysApp()
janela.run()
