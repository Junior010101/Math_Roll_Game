import pygame

class Escrever():
    def __init__(self, text, font, font_sz, color, x, y):
        self.text = text
        self.font = font
        self.font_size = font_sz
        self.color = color
        self.cord = [x, y]

        self.text_font = pygame.font.Font(self.font, self.font_size)
        self.texto = self.text_font.render(self.text, True, self.color)
    
    def Draw_text(self):
        self.tela = pygame.display.get_surface()
        self.tela.blit(self.texto, (self.cord[0], self.cord[1]))
