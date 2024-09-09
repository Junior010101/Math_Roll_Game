#Importações
import pygame

class Desenhar_Obj(pygame.sprite.Sprite):
    def __init__(self, local_imagem, pos, block_width, block_height, *groups):
        super().__init__(*groups)
        self.imagem = local_imagem
        self.size = [block_width, block_height]

        #importação da imagem
        self.img = pygame.image.load(self.imagem).convert_alpha()
        self.image = pygame.transform.scale(self.img, (self.size[0], self.size[1]))

        #Criação do objeto
        self.rect = self.image.get_rect(topleft= pos)
        