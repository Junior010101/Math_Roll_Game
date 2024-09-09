#Importações
import pygame

class Buttao(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        #Definições
        self.click = False
        self.count = 0

        #import de imagem
        btn_img = pygame.image.load("IMG/Start_btn.png").convert_alpha()
        self.btn_i = btn_img.subsurface((256, 0), (256, 66))
        self.btn_e = btn_img.subsurface((0, 0), (256, 66))

        #Criação de Sprites
        self.btn_imagems = []
        self.btn_imagems.append(self.btn_i)
        self.btn_imagems.append(self.btn_e)

        self.image = self.btn_imagems[self.count]

        self.rect = self.image.get_rect(topleft= pos)

    def interacao(self):
        #Descobrir a posição do mouse
        mouse_pos = pygame.mouse.get_pos()
        
        #Import de Som
        btn_sound = pygame.mixer.Sound("SOUND/Som_BTN_Start.mp3")

        #Se o usuario interagir com o botão
        if self.rect.collidepoint(mouse_pos):
            self.count = 1
            pygame.mouse.set_cursor(11)

            #Se o usuario clicar o botão
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                btn_sound.play()
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False
        
        #Se o usuario parar de interagir com o botão
        else:
            self.count = 0
            pygame.mouse.set_cursor(0)

    def update(self):
        self.interacao()
