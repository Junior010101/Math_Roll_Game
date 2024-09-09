#Importações
import pygame
from PYTHON.config import *
from PYTHON.botao import Buttao
from PYTHON.desenhar import Desenhar_Obj
from PYTHON.escrever import Escrever

class Menu_Principal():
    def __init__(self):
        #Definições
        self.tela = pygame.display.get_surface()
        self.show_sprites = pygame.sprite.Group()

        #Config de tela cheia
        Largura_Full = self.tela.get_width()
        Altura_Full = self.tela.get_height()

        #Configuração do fundo
        self.fundo_tela = Desenhar_Obj("IMG/Start_background.png", [0, 0], Largura_Full + 800, Altura_Full + 400, [self.show_sprites])

        #Importações de objetos
        self.botao = Buttao([560, 570] ,[self.show_sprites])
        self.dado = Desenhar_Obj("IMG/dado.png", [456, 95], 240, 205, [self.show_sprites])

        #Importações de textos
        self.math = Escrever("M   TH", "FONT/Pixil5.ttf", 180, "black", 380, 100)
        self.roll = Escrever("ROLL", "FONT/Pixil5.ttf", 120, "black", 725, 250)

    def run(self):
        #desenhar / animar na tela
        self.show_sprites.draw(self.tela)
        self.math.Draw_text()
        self.roll.Draw_text()
        self.show_sprites.update()
