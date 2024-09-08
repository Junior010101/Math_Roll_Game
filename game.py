#Importações
import pygame, sys

#Tela
pygame.init()
tela = pygame.display.set_mode((800, 400), pygame.RESIZABLE)

#Tela Cheia
Largura = tela.get_width()
Altura = tela.get_height()

#Logar Imagem da tela
img_tela = pygame.image.load("IMG/Start_background.png").convert_alpha()
fundo_tela = pygame.transform.scale(img_tela, (Largura + 800, Altura + 400))

def reload():
    tela.fill((255, 255, 255))
    pygame.display.update()

#Logar Som do botão
btn_sound = pygame.mixer.Sound("SOUND/Som_BTN_Start.mp3")

#Logar as Imagem do botão
btn_img = pygame.image.load("IMG/Start_btn.png").convert_alpha()
btn_e = btn_img.subsurface((0, 0), (256, 66))
btn_i = btn_img.subsurface((256, 0), (256, 66))

#Configuração do Botão de Start
class Buttao():
    def __init__(self, x, y, image):
        self.image = image
        self.click = False
        self.rect = pygame.Rect((x, y, 250, 60))

    def drawl(self):
        global Butao_imagem
        #Definir a posição do mouse na tela
        mouse_posição = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_posição):
            #Se o usuario passar o cursor sobre o botão
            Butao_imagem = Start_btn_e
            pygame.mouse.set_cursor(11)

            #Se o usuario clicar no botão
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                btn_sound.play()

            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False

            #Revertendo alterações
        else:
            Butao_imagem = Start_btn_i
            pygame.mouse.set_cursor(0)

        #Desenhar Objeto na Tela
        tela.blit(self.image, (self.rect.x, self.rect.y))

#Definição dos (Parametros) da Classe Botão
Start_btn_i = Buttao(560, 568, btn_i)
Start_btn_e = Buttao(560, 568, btn_e)
Butao_imagem = Start_btn_i

#Configuração do Draw Text
class Escrever():
    def __init__(self, text, font, font_sz, color, x, y):
        self.text = text
        self.font = font
        self.font_size = font_sz
        self.color = color
        self.cord = [x, y]

    def drawl_text(self):
        text_font = pygame.font.Font(self.font, self.font_size)
        texto = text_font.render(self.text, True, self.color)
        tela.blit(texto, (self.cord[0], self.cord[1]))

#Definição dos (Parametros) da Classe Escrever
Logo_Math = Escrever("M   TH", "FONT/Pixil5.ttf", 180, (0, 0, 0), 380, 100)
Logo_Roll = Escrever("ROLL", "FONT/Pixil5.ttf", 120, (0, 0, 0), 725, 250)

#Configuração do Draw obj
class Desenhar_objeto():
    def __init__(self, x, y , local_imagem, block_width, block_height):
        self.imagem = local_imagem
        self.rect = pygame.Rect((x, y, block_width, block_height))
        self.cord = [x, y]
        self.size = [block_width, block_height]

    def drawl_obj(self):
        self.img = pygame.image.load(self.imagem).convert_alpha()
        self.image = pygame.transform.scale(self.img, (self.size[0], self.size[1]))
        tela.blit(self.image, (self.cord[0], self.cord[1]))

#Deefinição dos (Parametros) da Classe Logo_Dado
Logo_Dado = Desenhar_objeto(456, 95, "IMG/dado.png", 240, 205)

#Menu Principal
def Menu_Principal():
    #Game Loop
    Menu_Run = True
    while Menu_Run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                reload()
                Menu_Run = False

        #Estilização da tela
        tela.fill((0, 0, 0))
        tela.blit(fundo_tela, (0, 0))

        #Adição do Botão
        Butao_imagem.drawl()

        #Adição da logo
        Logo_Math.drawl_text()
        Logo_Roll.drawl_text()
        Logo_Dado.drawl_obj()

Menu_Principal()

#Menu Secundario
def Menu_Select():
    #Game Loop
    Menu_Run = True
    while Menu_Run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                reload()
                Menu_Run = False

        tela.fill((0, 0, 0))
        

Menu_Select()

