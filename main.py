#Importações
from PYTHON.menu import Menu_Principal
from PYTHON.config import *
import pygame, sys

#Inicio do jogo
class Jogo():
    def __init__(self):
        #Inicializando o Pygame
        pygame.init()
        pygame.display.set_caption(Nome_Jogo)
        self.tela = pygame.display.set_mode((Largura_Janela, Altura_Janela), pygame.RESIZABLE)
        self.Fps = pygame.time.Clock()

        self.menu = Menu_Principal()
                
    def run(self):
        #Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.tela.fill("black")
            self.menu.run()
            pygame.display.flip()
            self.Fps.tick(Taxa_Atualizacao)

if __name__ == "__main__":
    jogo = Jogo()
    jogo.run()
