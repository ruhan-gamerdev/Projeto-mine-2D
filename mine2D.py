import pygame
import os
import pickle
from random import randint
from time import sleep

#------------- CORES -------------
azul = (0, 190, 255)
ciano = (0, 255, 255)
marron = (255, 120, 0)
verde = (0, 255, 0)
cinza = (120, 120, 120)
cinza_esq = (50, 50, 50)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
preto = (0, 0, 0)
bt = (100, 100, 255)
btq = vermelho
btq2 = vermelho
    
#-------------- INIT ----------------
pygame.init()
tela = pygame.display.set_mode((1475, 720))

#--------- BTN_TRANS ---------
# cria uma surface com suporte a transparência
ret_surface = pygame.Surface((200, 160), pygame.SRCALPHA)
# desenha o retângulo com alpha (RGBA)
pygame.draw.rect(ret_surface, (120, 120, 255, 100), (0, 0, 200, 160))

#----------- CONFIG ------------
zero = 0
m = 60
x = 0
l = False
l2 = False
v = 0
v2 = 5
mg = 2
clock = pygame.time.Clock()
fps = 60
fip = False
dre = ">"
block = None
bloc_pedr = zero
bloc_gram = zero
bloc_made = zero
bloc_tabo = zero
bloc_port = zero+10
h = 700-(75*3)
h2 = 85
h3 = h
no_chao = False
tip_constr = None
arv = randint(0, 100)
cav = randint(0, 5)
fer = randint(0, 10)
pode = True
rende = 3 # MAX 7, NORM 3, MIN 1
render = (rende * 100) + 1
carvoes = []
ferros = []
mobs = []
inventario = False
itm_ferr = 0
itm_carv = 0
itm_estk = 0
tenp = 0.1
t = 0
menu = True

#------------ BUTÃO ------------
btn_esq = pygame.Rect(10, 550, 200, 160)
btn_dir = pygame.Rect(220, 550, 200, 160)
btn_que = pygame.Rect(1265, 550, 200, 160)
btn_que2 = pygame.Rect(1265-205, 550, 200, 160)
btn_rot = pygame.Rect(h, 40, 75, 75)
btn_rot2 = pygame.Rect(h+h2, 40, 75, 75)
btn_rot3 = pygame.Rect(h+(h2*2), 40, 75, 75)
btn_rot4 = pygame.Rect(h+(h2*3), 40, 75, 75)
btn_rot5 = pygame.Rect(h+(h2*4), 40, 75, 75)
btn_invit = pygame.Rect(1401, 0, 75, 75)
btn_men = pygame.Rect((1500/2)-(300/2), 100, 300, 100)
btn_men2 = pygame.Rect((1500/2)-(300/2), 250, 300, 100)
btn_men3 = pygame.Rect((1500/2)-(300/2), 400, 300, 100)
btn_menu = pygame.Rect((0, 0, 75, 75))
btn_invit_made = pygame.Rect(((50+(85*3))+5, 50, 75, 75))
btn_invit_tabo = pygame.Rect(((50+(85*2))+5, 50, 75, 75))
btn_invti_estk = pygame.Rect(((50+(85*4))+5, 50, 75, 75))
btn_crt1 = pygame.Rect((750, m, 75, 75))
btn_crt2 = pygame.Rect((750+80, m, 75, 75))
btn_crt3 = pygame.Rect((750+(80*2), m, 75, 75))
btn_crt4 = pygame.Rect((750, m+80, 75, 75))
btn_crt5 = pygame.Rect((750+80, m+80, 75, 75))
btn_crt6 = pygame.Rect((750+(80*2), m+80, 75, 75))
btn_crt7 = pygame.Rect((750, m+(80*2), 75, 75))
btn_crt8 = pygame.Rect((750+80, m+(80*2), 75, 75))
btn_crt9 = pygame.Rect((750+(80*2), m+(80*2), 75, 75))
btn_crtc = pygame.Rect((750+(80*4), m+80, 75, 75))
btn_crtc2 = pygame.Rect((750+(80*4), m, 75, 75))

#-------------- IMG --------------
grama = pygame.image.load("img/grama.png").convert_alpha()
grama_img = pygame.transform.scale(grama, (75, 75))
grama_img2 = pygame.transform.scale(grama, (1500, 750))

pedra = pygame.image.load("img/pedra.png").convert_alpha()
pedra_img = pygame.transform.scale(pedra, (75, 75))

pedra2 = pygame.image.load("img/bedrok.png").convert_alpha()
pedra2_img = pygame.transform.scale(pedra2, (75, 75))

player_fren = pygame.image.load("img/player_fen.png").convert_alpha()
player2_img = pygame.transform.scale(player_fren, (60, 100))

ceu = pygame.image.load("img/ceu.png").convert_alpha()
ceu_img = pygame.transform.scale(ceu, (75, 75))
    
madeira = pygame.image.load("img/madeira.png").convert_alpha()
madeira_img = pygame.transform.scale(madeira, (75, 75))

folha = pygame.image.load("img/folha.png").convert_alpha()
folha_img = pygame.transform.scale(folha, (75, 75))

carvao = pygame.image.load("img/carvão.png").convert_alpha()
carvao_img = pygame.transform.scale(carvao, (75, 75))

carvao_item = pygame.image.load("img/carvão_item.png").convert_alpha()
carvao_item_img = pygame.transform.scale(carvao_item, (75, 75))

ferro = pygame.image.load("img/ferro.png").convert_alpha()
ferro_img = pygame.transform.scale(ferro, (75, 75))

ferro_item = pygame.image.load("img/ferro_item.png").convert_alpha()
ferro_item_img = pygame.transform.scale(ferro_item, (75, 75))

inventario_im = pygame.image.load("img/inventário.png").convert_alpha()
inventario_img = pygame.transform.scale(inventario_im, (75, 75))

menu_pot = pygame.image.load("img/menu_°°°.png").convert_alpha()
menu_pot_img = pygame.transform.scale(menu_pot, (75, 75))

taboa = pygame.image.load("img/taboa.png").convert_alpha()
taboa_img = pygame.transform.scale(taboa, (75, 75))

graveto = pygame.image.load("img/graveto.png").convert_alpha()
graveto_img = pygame.transform.scale(graveto, (75, 75))

porta = pygame.image.load("img/porta.png").convert_alpha()
porta_img = pygame.transform.scale(porta, (75, 75))

porta_c = pygame.image.load("img/porta↑.png").convert_alpha()
porta_c_img = pygame.transform.scale(porta_c, (75, 75))

porta_b = pygame.image.load("img/porta↓.png").convert_alpha()
porta_b_img = pygame.transform.scale(porta_b, (75, 75))

porta_b2 = pygame.image.load("porta_pst/porta_↓°.png").convert_alpha()
porta_b2_img = pygame.transform.scale(porta_b2, (75, 75))

porta_c2 = pygame.image.load("porta_pst/porta_↑°.png").convert_alpha()
porta_c2_img = pygame.transform.scale(porta_c2, (75, 75))

graveto = pygame.image.load("img/graveto.png").convert_alpha()
graveto_img = pygame.transform.scale(graveto, (75, 75))

vaca = pygame.image.load("img/vaca.png").convert_alpha()
vaca_img = pygame.transform.scale(vaca, (150, 90))

#--------- CONF_IMG ----------
bloc_constr = grama_img
craft = {
    "1": {
        "1": ceu_img,
        "2": ceu_img,
        "3": ceu_img,
        },
     "2": {
        "1": ceu_img,
        "2": ceu_img,
        "3": ceu_img,
        },
    "3": {
        "1": ceu_img,
        "2": ceu_img,
        "3": ceu_img,
        }
    }
craf = ceu_img

#-------- CONF_CAM ---------
camera_x = 0
camera_y = 0

#----------- PLAYER ------------
tam1 = 120
tam2 = 100
player = pygame.Rect(50, 10, 50, 100)
player_1 = pygame.image.load("img/player.png").convert_alpha()
player_img = pygame.transform.scale(player_1, (tam1, tam2))
player_x = player.x
player_y = player.y

#-------- DEFs/CLASSs ---------
def blocos_proximos(player, lista, margem=150):#150
    proximos = []
    for b in lista:
        rect = b["rect"] if isinstance(b, dict) else b
        if abs(rect.x - player.x) < margem and abs(rect.y - player.y) < margem:
            proximos.append(b)
    return proximos

def salvar_mundo():
    if not os.path.exists("mundo_salvo"):
        os.makedirs("mundo_salvo")

    dados = {
        "mund": [
            {
                "x": b["rect"].x,
                "y": b["rect"].y,
                "tipo": "ceu" if b["img"] == ceu_img else
                        "grama" if b["img"] == grama_img else
                        "pedra" if b["img"] == pedra_img else
                        "madeira" if b["img"] == madeira_img else
                        "taboa" if b["img"] == taboa_img else
                        "porta↓" if b["img"] == porta_b_img else
                        "porta↑" if b["img"] == porta_c_img else
                        "porta↓" if b["img"] == porta_b2_img else
                        "porta↑" if b["img"] == porta_c2_img else
                        "folha"
            }
            for b in mund
        ],
        "chao_pedra": [
            {
                "x": b["rect"].x,
                "y": b["rect"].y,
                "tipo": "pedra" if b["img"] == pedra_img else
                        "carvao" if b["img"] == carvao_img else
                        "ferro"
            }
            for b in chao_pedra
        ],
        "chao_grama": [
            {
                "x": b.x,
                "y": b.y,
            }
            for b in chao_grama
        ],
        "inventario": {
            "grama": bloc_gram,
            "pedra": bloc_pedr,
            "madeira": bloc_made,
            "taboa": bloc_tabo,
            "porta": bloc_port,
            "carvao": itm_carv,
            "ferro": itm_ferr,
            "graveto": itm_estk
        },
        "player": {
            "x": player.x,
            "y": player.y
        }
    }

    with open("mundo_salvo/mundo.pkl", "wb") as arquivo:
        pickle.dump(dados, arquivo)

    print("Mundo salvo com sucesso!")

def carregar_mundo():
    global mund, chao_pedra,chao_grama,bloc_gram, bloc_pedr, bloc_made, bloc_tabo, bloc_port
    global itm_carv, itm_ferr, player

    if not os.path.exists("mundo_salvo/mundo.pkl"):
        print("Nenhum save encontrado!")
        return

    with open("mundo_salvo/mundo.pkl", "rb") as arquivo:
        dados = pickle.load(arquivo)

    # LIMPA O MUNDO ATUAL
    mund.clear()
    chao_pedra.clear()
    chao_grama.clear()

    # ---------- RECONSTRÓI MUND ----------
    for b in dados["mund"]:
        if b["tipo"] == "ceu":
            img = ceu_img
        elif b["tipo"] == "grama":
            img = grama_img
        elif b["tipo"] == "pedra":
            img = pedra_img
        elif b["tipo"] == "madeira":
            img = madeira_img
        elif b["tipo"] == "taboa":
            img = taboa_img
        elif b["tipo"] == "porta↑":
            img = porta_c_img
        elif b["tipo"] == "porta↓":
            img = porta_b_img
        else:
            img = folha_img

        mund.append({
            "rect": pygame.Rect(b["x"], b["y"], 75, 75),
            "img": img
        })

    # --------- RECONSTRÓI CHÃO GRAMA ----------
    for b in dados["chao_grama"]:
        chao_grama.append(pygame.Rect(b["x"], b["y"], 75, 75))

    # ---------- RECONSTRÓI CHÃO PEDRA ----------
    for b in dados["chao_pedra"]:
        if b["tipo"] == "pedra":
            img = pedra_img
        elif b["tipo"] == "carvao":
            img = carvao_img
        else:
            img = ferro_img

        chao_pedra.append({
            "rect": pygame.Rect(b["x"], b["y"], 75, 75),
            "img": img
        })

    # ---------- INVENTÁRIO ----------
    bloc_gram = dados["inventario"]["grama"]
    bloc_pedr = dados["inventario"]["pedra"]
    bloc_made = dados["inventario"]["madeira"]
    bloc_tabo = dados["inventario"]["taboa"]
    bloc_port = dados["inventario"]["porta"]
    itm_carv = dados["inventario"]["carvao"]
    itm_ferr = dados["inventario"]["ferro"]
    ifm_estk = dados["inventario"]["graveto"]

    # ---------- PLAYER ----------
    player.x = dados["player"]["x"]
    player.y = dados["player"]["y"]

    print("Mundo carregado com sucesso!")

class Carvao():
    def __init__(self, p_x, p_y, img):
        self.p_x = p_x
        self.p_y = p_y
        self.img = img
        self.num = 0
        self.dire = "v"
    
    def most(self, camera_x, camera_y):
        tela.blit(self.img, (self.p_x - camera_x, self.p_y - camera_y))
    
    def mover(self):
        if self.num >= 3:
            self.dire = "^"
        elif self.num <= -10:
            self.dire = "v"
        #
        if self.dire == "^":
            self.p_y -= 1
            self.num -= 1.5
        elif self.dire == "v":
            self.p_y += 1
            self.num += 1.5
    
    def colid(self):
        self.rect = pygame.Rect((self.p_x+20), (self.p_y+20), 40, 50)
        if self.rect.colliderect(player):
            self.sumir = True
            return True
        else:
            self.sumir = False
            return False
            
class Ferro():
    def __init__(self, p_x, p_y, img):
        self.p_x = p_x
        self.p_y = p_y
        self.img = img
        self.num = 0
        self.dire = "v"
    
    def most(self, camera_x, camera_y):
        tela.blit(self.img, (self.p_x - camera_x, self.p_y - camera_y))
    
    def mover(self):
        if self.num >= 3:
            self.dire = "^"
        elif self.num <= -10:
            self.dire = "v"
        #
        if self.dire == "^":
            self.p_y -= 1
            self.num -= 1.5
        elif self.dire == "v":
            self.p_y += 1
            self.num += 1.5
    
    def colid(self):
        self.rect = pygame.Rect((self.p_x+20), (self.p_y+20), 40, 50)
        if self.rect.colliderect(player):
            self.sumir = True
            return True
        else:
            self.sumir = False
            return False

class mob():
    def __init__(self, img):
        self.img = img
        self.posx = randint(-15400, 15400)
        self.posy = 200
        self.m = randint(1, 4)
        self.vely = 0
        self.rect = pygame.Rect((self.posx, self.posy,150, 90))
        
    def sort(self):
        self.m = randint(1, 4) 
        if self.m == 1:
            self.m = 5
        elif self.m == 2:
            self.m = -5
        else:
            self.m = 0
            
    def mov(self):
        self.posx += self.m
        
    def most(self, tela, camera_x, camera_y):
        self.rect.x = self.posx
        self.rect.y = self.posy
        #pygame.draw.rect(tela, (255, 0, 0), (self.posx-camera_x, self.posy-camera_y, 150, 90))
        tela.blit(self.img, (self.rect.x-camera_x, self.rect.y-camera_y))
        
    def gravidade(self, mund, chao_grama, chao_pedra, chao_pedra2):
        self.rect = pygame.Rect(self.posx, self.posy, 150, 90)
        no_chao = False
    
        for lista in [mund, chao_grama, chao_pedra, chao_pedra2]:
            for b in blocos_proximos(self.rect, lista, margem=105):
                if lista == chao_pedra:
                    rect = b["rect"]
                elif lista == mund:
                    if b["img"] == ceu_img:
                        continue
                    rect = b["rect"]
                else:
                    rect = b
    
                if self.rect.colliderect(rect):
                    no_chao = True
                    self.posy = rect.top - 90
                    self.vely = 0
                    break
            if no_chao:
                break
    
        if not no_chao:
            if self.vely <= 50:
                self.vely += 0.7
            self.posy += self.vely
    
    def perto_do_player(self, player, distancia=render):
        dx = player.centerx - self.rect.centerx
        dy = player.centery - self.rect.centery
        dist = (dx**2 + dy**2) ** 0.5
        return dist < distancia
    
#------------ CHAOS ------------
chao_grama = []
chao_pedra = []
chao_pedra2 = []
mund = []
arvores = []

# GRAMA
x = -(75*100)
for i in range(220):#20
    chao_grama.append(pygame.Rect(x, 355, 75, 75))
    x += 75

# PEDRA
x = -(75*100)
y = 425
for a in range(39):#3
    for e in range(220):#220
        chao_pedra.append({
            "rect": pygame.Rect(x, y, 75, 75),
            "img": pedra_img
        })
        x += 75
    y += 75
    x = -(75*100)

# BEDROK
x = -(75*100)
for i in range(220):#220
    chao_pedra2.append(pygame.Rect(x, (355+(75*40))-5, 75, 75))
    x += 75

# CONSTR
x = -(75*100)
y = -20-(75*5)#-20
for a in range(30):#14
    for e in range(220):#220
        mund.append({
            "rect": pygame.Rect(x, y, 75, 75),
            "img": ceu_img
        })
        x += 75
    y += 75
    x = -(75*100)
    
# ARVORE
for b in mund:
    if b['rect'].y == (75*4)-20:

        arv = randint(0, 100)
        pode = True

        for ax in arvores:
            if abs(b["rect"].x - ax) < 75 * randint(8, 15):
                pode = False
                break

        if arv >= 30 and pode:
            b["img"] = madeira_img
            arvores.append(b["rect"].x)

            for outro in mund:
                if (outro["rect"].x == b["rect"].x and
                    outro["rect"].y == b["rect"].y - 75):
                    outro["img"] = madeira_img

                if (outro["rect"].x == b["rect"].x and
                    outro["rect"].y == b["rect"].y - (75*2)):
                    outro["img"] = folha_img
                    
                if (outro["rect"].x == b["rect"].x - 75 and
                    outro["rect"].y == b["rect"].y - (75*2)):
                    outro["img"] = folha_img
                
                if (outro["rect"].x == b["rect"].x + 75 and
                    outro["rect"].y == b["rect"].y - (75*2)):
                    outro["img"] = folha_img

                if (outro["rect"].x == b["rect"].x and
                    outro["rect"].y == b["rect"].y - (75*3)):
                    outro["img"] = folha_img
                
                if (outro["rect"].x == b["rect"].x - 75 and
                    outro["rect"].y == b["rect"].y - (75*3)):
                    outro["img"] = folha_img
                
                if (outro["rect"].x == b["rect"].x + 75 and
                    outro["rect"].y == b["rect"].y - (75*3)):
                    outro["img"] = folha_img
                
                if (outro["rect"].x == b["rect"].x and
                    outro["rect"].y == b["rect"].y - (75*4)):
                    outro["img"] = folha_img
                
# CARVÃO
for b in chao_pedra:
    cav = randint(0,5)
    if cav >= 4:
        b["img"] = carvao_img
        
# FERRO
for b in chao_pedra:
    fer = randint(0, 10)
    if fer >= 10:
        b["img"] = ferro_img

mapa = pygame.Surface(tela.get_size(), pygame.SRCALPHA)

for b in mund:
    mapa.blit(b["img"], b["rect"])
    
for b in chao_grama:
    mapa.blit(grama_img, b)

for b in chao_pedra:
    mapa.blit(b["img"], b["rect"])
    
for b in chao_pedra2:
    mapa.blit(pedra2_img, b)
    
#----------- TEXTO --------------
fonte = pygame.font.SysFont("arial", 40, True, True)

# ------ CLASS_INIT ----------
#mob1 = mob()
#mobs.append(mob(vaca_img))
###

#------------ LOOP ---------------
while True:
    # MAUSE
    mause_pos = pygame.mouse.get_pos()
    mause_pos2 = (
        mause_pos[0] + camera_x,
        mause_pos[1] + camera_y
    )
    mause_click = pygame.mouse.get_pressed()[0]
    
    
    # ------------ MENU -----------
    while menu:
        tela.fill(verde)
        
        # MAUSE
        mause_pos = pygame.mouse.get_pos()
        mause_pos2 = (
            mause_pos[0] + camera_x,
            mause_pos[1] + camera_y
        )
        mause_click = pygame.mouse.get_pressed()[0]
        
        # ---------- DESENHO -----------
        tela.blit(grama_img2, (0, 0))
        pygame.draw.rect(tela, cinza, btn_men)
        pygame.draw.rect(tela, cinza, btn_men2)
        pygame.draw.rect(tela, cinza, btn_men3)
        
        # ------------ BUTÃO --------------
        if btn_men.collidepoint(mause_pos):
            menu = False
        
        if btn_men2.collidepoint(mause_pos):
            salvar_mundo()
            menu = False
            sleep(tenp)
        
        if btn_men3.collidepoint(mause_pos):
            carregar_mundo()
            menu = False
            sleep(tenp)
        ###
        
        pygame.display.update()
    
    
    if btn_invit.collidepoint(mause_pos) and mause_click:
        if inventario:
            inventario = False
            sleep(tenp)
        else:
            inventario = True
            sleep(tenp)
    # -------------- INVIT --------------
    if inventario:
        while inventario:
            tela.fill(cinza_esq)
            
            # MAUSE
            mause_pos = pygame.mouse.get_pos()
            mause_click = pygame.mouse.get_pressed()[0]
            
            # -------- DESENHO -----------
            if craft["1"]["1"] == taboa_img and craft["1"]["2"] == taboa_img and craft["2"]["1"] == taboa_img and craft["2"]["2"] == taboa_img and craft["3"]["1"] == taboa_img and craft["3"]["2"] == taboa_img:
                if bloc_tabo >= 6:
                    tela.blit(porta_img, (btn_crtc.x, btn_crtc.y))
            
            
            
            elif craft["2"]["2"] == madeira_img:
                tela.blit(taboa_img, (btn_crtc.x, btn_crtc.y))
            
            elif craft["3"]["2"] == taboa_img and craft["2"]["2"] == taboa_img:
                tela.blit(graveto_img, (btn_crtc.x, btn_crtc.y))
            # INVENTARIO
            #pygame.draw.rect(tela, vermelho, btn_invit)
            tela.blit(inventario_img, (btn_invit.x, btn_invit.y))
            # - CRAFT -
            i = 750
            i2 = 50
            pygame.draw.rect(tela, cinza_esq, (i, i2, 75+15, 75+15))
            pygame.draw.rect(tela, cinza, (i, i2+10, 75, 75))
            pygame.draw.rect(tela, cinza_esq, (i+(75+5), i2, 75+15, 75+15))
            pygame.draw.rect(tela, cinza, (i+(75+5), i2+10, 75, 75))
            pygame.draw.rect(tela, cinza_esq, (i+((75+5)*2), i2, 75+15, 75+15))
            pygame.draw.rect(tela, cinza, (i+((75+5)*2), i2+10, 75, 75))
            #
            i2 = 50+80
            pygame.draw.rect(tela, cinza_esq, (i, i2, 75+15, 75+15))
            pygame.draw.rect(tela, cinza, (i, i2+10, 75, 75))
            pygame.draw.rect(tela, cinza_esq, (i+(75+5), i2, 75+15, 75+15))
            pygame.draw.rect(tela, cinza, (i+(75+5), i2+10, 75, 75))
            pygame.draw.rect(tela, cinza_esq, (i+((75+5)*2), i2, 75+15, 75+15))
            pygame.draw.rect(tela, cinza, (i+((75+5)*2), i2+10, 75, 75))
            #
            i2 = 50+(80*2)
            pygame.draw.rect(tela, cinza_esq, (i, i2, 75+15, 75+15))
            pygame.draw.rect(tela, cinza, (i, i2+10, 75, 75))
            pygame.draw.rect(tela, cinza_esq, (i+(75+5), i2, 75+15, 75+15))
            pygame.draw.rect(tela, cinza, (i+(75+5), i2+10, 75, 75))
            pygame.draw.rect(tela, cinza_esq, (i+((75+5)*2), i2, 75+15, 75+15))
            pygame.draw.rect(tela, cinza, (i+((75+5)*2), i2+10, 75, 75))
            #
            #pygame.draw.rect(tela, bt, btn_crt1)
            #pygame.draw.rect(tela, bt, btn_crt2)
            #pygame.draw.rect(tela, bt, btn_crt3)
            #pygame.draw.rect(tela, bt, btn_crt4)
            #pygame.draw.rect(tela, bt, btn_crt5)
            #pygame.draw.rect(tela, bt, btn_crt6)
            #pygame.draw.rect(tela, bt, btn_crt7)
            #pygame.draw.rect(tela, bt, btn_crt8)
            #pygame.draw.rect(tela, bt, btn_crt9)
            #pygame.draw.rect(tela, bt, btn_crtc)
            pygame.draw.rect(tela, bt, btn_crtc2)
            
            #---- IMG ----
            # ITEM
            if itm_carv != 0:
                tela.blit(carvao_item_img, (50, 50))
            if itm_ferr != 0:
                tela.blit(ferro_item_img, (50+85, 50))
            if itm_estk != 0:
                tela.blit(graveto_img, (50+(85*4), 50))
            
            # BLOC
            #pygame.draw.rect(tela, bt, btn_invit_made)
            #pygame.draw.rect(tela, bt, btn_invit_tabo)
            if bloc_tabo != 0:
                pd_tabo = True
                tela.blit(taboa_img, ((50+(85*2))+5, 50))
            else:
                pd_tabo = False
            
            if bloc_made != 0:
                tela.blit(madeira_img, (btn_invit_made))
                pd_made = True
            else:
                pd_made = False

            if craft["1"]["1"] != ceu_img:
                tela.blit(craft["1"]["1"], (750, 60))
            if craft["1"]["2"] != ceu_img:
                tela.blit(craft["1"]["2"], (750+80, 60))
            if craft["1"]["3"] != ceu_img:
                tela.blit(craft["1"]["3"], (750+(80*2), 60))
                
            if craft["2"]["1"] != ceu_img:
                tela.blit(craft["2"]["1"], (750, 60+80))
            if craft["2"]["2"] != ceu_img:
                tela.blit(craft["2"]["2"], (750+80, 60+80))
            if craft["2"]["3"] != ceu_img:
                tela.blit(craft["2"]["3"], (750+(80*2), 60+80))
            
            if craft["3"]["1"] != ceu_img:
                tela.blit(craft["3"]["1"], (750, 60+(80*2)))
            if craft["3"]["2"] != ceu_img:
                tela.blit(craft["3"]["2"], (750+80, 60+(80*2)))
            if craft["3"]["3"] != ceu_img:
                tela.blit(craft["3"]["3"], (750+(80*2), 60+(80*2)))
            
            # TEXTO
            mensagem_inv = f"{itm_carv}"
            texto_form_inv = fonte.render(mensagem_inv, True, (255, 255, 255))
            
            mensagem_inv1 = f"{itm_ferr}"
            texto_form_inv1 = fonte.render(mensagem_inv1, True, (255, 255, 255))
            
            mensagem_inv2 = f"{bloc_tabo}"
            texto_form_inv2 = fonte.render(mensagem_inv2, True, (255, 255, 255))
            
            mensagem_inv3 = f"{bloc_made}"
            texto_form_inv3 = fonte.render(mensagem_inv3, True, (255, 255, 255))
            
            mensagem_inv4 = f"{itm_estk}"
            texto_form_inv4 = fonte.render(mensagem_inv4, True, (255, 255, 255))
            
            if itm_carv != 0:
                tela.blit(texto_form_inv, (90, 70))
            if itm_ferr != 0:
                tela.blit(texto_form_inv1, (90+85, 70))
            if bloc_tabo != 0:
                tela.blit(texto_form_inv2, (90+(85*2), 70))
            if bloc_made != 0:
                tela.blit(texto_form_inv3, (90+(85*3), 70))
            if itm_estk != 0:
                tela.blit(texto_form_inv4, (90+(85*4), 70))
            
            # ----------- BOTÃO -----------
            #CRAFT
            if btn_crt1.collidepoint(mause_pos):
                craft["1"]["1"] = craf
            
            if btn_crt2.collidepoint(mause_pos):
                craft["1"]["2"] = craf
            
            if btn_crt3.collidepoint(mause_pos):
                craft["1"]["3"] = craf
            
            if btn_crt4.collidepoint(mause_pos):
                craft["2"]["1"] = craf
            
            if btn_crt5.collidepoint(mause_pos):
                craft["2"]["2"] = craf
            
            if btn_crt6.collidepoint(mause_pos):
                craft["2"]["3"] = craf
            
            if btn_crt7.collidepoint(mause_pos):
                craft["3"]["1"] = craf
            
            if btn_crt8.collidepoint(mause_pos):
                craft["3"]["2"] = craf
            
            if btn_crt9.collidepoint(mause_pos):
                craft["3"]["3"] = craf
            
            if btn_crtc.collidepoint(mause_pos) and mause_click:
                if craft["3"]["2"] == taboa_img and craft["2"]["2"] == taboa_img:
                    if bloc_tabo >= 2:
                        bloc_tabo -= 2
                        itm_estk += 4
                    
                elif craft["2"]["2"] == madeira_img:
                    if bloc_made != 0:
                        bloc_made -= 1
                        bloc_tabo += 4
                elif craft["1"]["1"] == taboa_img and craft["1"]["2"] == taboa_img and craft["2"]["1"] == taboa_img and craft["2"]["2"] == taboa_img and craft["3"]["1"] == taboa_img and craft["3"]["2"] == taboa_img:
                    if bloc_tabo >= 6:
                         bloc_tabo -= 6
                         bloc_port += 2
                         
                sleep(tenp)
                #for linha in craft.values():
                    #for valor in linha.values():
                        #if valor == madeira_img:
                            #if bloc_made != 0:
                                #bloc_tabo += 4
                                #bloc_made -=1
                                #sleep(tenp)
                            #break
            
            if btn_crtc2.collidepoint(mause_pos) and mause_click:
                craf = ceu_img
            #
            
            if btn_invit.collidepoint(mause_pos) and mause_click:
                if inventario:
                    inventario = False
                    sleep(tenp)
                else:
                    inventario = True
                    sleep(tenp)
                    
            if btn_invit_made.collidepoint(mause_pos) and mause_click and pd_made:
                if bloc_made != 0:
                    #bloc_made -= 1
                    #bloc_tabo += 4
                    craf = madeira_img
                    sleep(tenp)
                else:
                    sleep(tenp)
            
            if btn_invit_tabo.collidepoint(mause_pos) and mause_click:
                if bloc_tabo != 0:
                    craf = taboa_img
            
            if btn_invti_estk.collidepoint(mause_pos) and mause_click:
                if itm_estk != 0:
                    craf = graveto_img
            
            pygame.display.update()
            
            #####
    
    # -------------- JOGO -------------
    clock.tick(fps)
    tela.fill(azul)
    
    #---------- TEST -----------
    #tela.blit(carvao_item_img, (0, 0))

    #--------- MOVIMENTO --------
    if btn_dir.collidepoint(mause_pos) and mause_click:
        if dre != ">":
            fip = True
            player_1 = pygame.transform.flip(player_1, fip, False)
        dre = ">"
        v2 += 0.5
        player.x += v2
        player_img = pygame.transform.scale(player_1, (tam1, tam2))
        mg = 1

    if btn_esq.collidepoint(mause_pos) and mause_click:
        if dre != "<":
            fip = True
            player_1 = pygame.transform.flip(player_1, fip, False)
        dre = "<"
        v2 += 0.5
        player.x -= v2
        player_img = pygame.transform.scale(player_1, (tam1, tam2))
        mg = 1
    
    if not mause_click:
        v2 = 5
        mg = 2
    # CAM
    camera_x = player.centerx - tela.get_width() // 2
    camera_y = player.centery - tela.get_height() // 2
    
    #----------- DESENHO ----------
    
    #--- ITENS ---
    # CARVÃO
    for carvao in carvoes:
        carvao.mover()
        carvao.most(camera_x, camera_y)
        if carvao.colid():
            carvoes.remove(carvao)
            itm_carv += 1
        #pygame.draw.rect(tela, (255, 0, 0), carvao.rect)
    
    # FERRO
    for ferro in ferros:
        ferro.mover()
        ferro.most(camera_x, camera_y)
        if ferro.colid():
            ferros.remove(ferro)
            itm_ferr += 1
        #pygame.draw.rect(tela, (255, 0, 0), ferro.rect)
    
    # TESTE
    ###
    
    # GRAMA, PEDRA
    #tela.blit(mapa, (0 - camera_x, 0 - camera_y))
    
    # -------- DESENHO DO CHÃO (OTIMIZADO) -------
    for lista in [mund, chao_grama, chao_pedra, chao_pedra2]:
        for b in blocos_proximos(player, lista, margem=render):
            if lista == mund:
                if b["img"] != ceu_img:
                    tela.blit(b["img"], (b["rect"].x - camera_x, b["rect"].y - camera_y))
                    pass
            if lista == chao_grama:
                tela.blit(grama_img, (b.x - camera_x, b.y - camera_y))
            if lista == chao_pedra:
                tela.blit(b["img"], (b["rect"].x - camera_x, b["rect"].y - camera_y))
            if lista == chao_pedra2:
                tela.blit(pedra2_img, (b.x - camera_x, b.y - camera_y))
    
    # PLAYER
    player_x = player.x - camera_x - 35
    player_y = player.y - camera_y
    #pygame.draw.rect(tela, vermelho, player)
    if mg == 1:
        tela.blit(player_img, (player_x, player_y))
    if mg == 2:
        player_x = player.x - camera_x - 5
        tela.blit(player2_img, (player_x, player_y))
    
    # ROT_BAR
    pygame.draw.rect(tela, cinza, (h-5, 35, (75*5)+(10*5), 75+10))
    pygame.draw.rect(tela, cinza_esq, (h3-5, 35, 75+10, 75+10))
    pygame.draw.rect(tela, cinza, (h3, 40, 75, 75))
    
    if bloc_gram != 0:
        tela.blit(grama_img, (h, 40))
    if bloc_pedr != 0:
        tela.blit(pedra_img, (h+h2, 40))
    if bloc_made != 0:
        tela.blit(madeira_img, (h+(h2*2), 40))
    if bloc_tabo != 0:
        tela.blit(taboa_img, (h+(h2*3), 40))
    if bloc_port != 0:
        tela.blit(porta_img, (h+(h2*4), 40))
    
    # TEXTO
    mensagem  = f"{bloc_gram}"
    texto_form = fonte.render(mensagem, True, (0, 0, 0))
    mensagem2  = f"{bloc_pedr}"
    texto_form2 = fonte.render(mensagem2, True, (0, 0, 0))
    mensagem3  = f"{bloc_made}"
    texto_form3 = fonte.render(mensagem3, True, (0, 0, 0))
    
    mensagem4  = f"{bloc_tabo}"
    texto_form4= fonte.render(mensagem4, True, (0, 0, 0))
    
    mensagem5  = f"{bloc_port}"
    texto_form5= fonte.render(mensagem5, True, (0, 0, 0))
    
    if bloc_gram != 0:
        tela.blit(texto_form, (h, 70))
    if bloc_pedr != 0:
        tela.blit(texto_form2, (h+h2, 70))
    if bloc_made != 0:
        tela.blit(texto_form3, (h+(h2*2), 70))
    if bloc_tabo != 0:
        tela.blit(texto_form4, (h+(h2*3), 70))
    if bloc_port != 0:
        tela.blit(texto_form5, (h+(h2*4), 70))
    
    #---- BOTÃO ----
    # MOV
    #pygame.draw.rect(tela, bt, btn_dir)
    tela.blit(ret_surface, (230, 550))
    #pygame.draw.rect(tela, bt, btn_esq)
    tela.blit(ret_surface, (10, 550))
    
    # ROT
    #pygame.draw.rect(tela, bt, btn_rot)
    #pygame.draw.rect(tela, bt, btn_rot2)
    #pygame.draw.rect(tela, bt, btn_rot3)
    #pygame.draw.rect(tela, bt, btn_rot4)
    #pygame.draw.rect(tela, bt, btn_rot5)
    
    # QUEBR
    pygame.draw.rect(tela, btq, btn_que)
    pygame.draw.rect(tela, btq2, btn_que2)
    
    # INVIT
    #pygame.draw.rect(tela, vermelho, btn_invit)
    tela.blit(inventario_img, (btn_invit.x, btn_invit.y))
    
    # MENU
    #pygame.draw.rect(tela, vermelho, btn_menu)
    tela.blit(menu_pot_img, (btn_menu.x, btn_menu.y))
    
    #----------- ROT_BAR -----------
    if btn_rot.collidepoint(mause_pos):
        bloc_constr = grama_img
        tip_constr = "grama"
        h3 = h
    
    if btn_rot2.collidepoint(mause_pos):
        bloc_constr = pedra_img
        tip_constr = "pedra"
        h3 = h+h2
        
    if btn_rot3.collidepoint(mause_pos):
        bloc_constr = madeira_img
        tip_constr = "madeira"
        h3 = h+(h2*2)
        
    if btn_rot4.collidepoint(mause_pos):
        bloc_constr = taboa_img
        tip_constr = "taboa"
        h3 = h+(h2*3)
        
    if btn_rot5.collidepoint(mause_pos):
        bloc_constr = porta_b_img
        tip_constr = "porta"
        h3 = h+(h2*4)
    
    # ----------- MENU --------------
    if btn_menu.collidepoint(mause_pos):
        menu = True
    
    # ----------- PORTA -------------
    for b in blocos_proximos(player, mund):
        if b["rect"].collidepoint(mause_pos2) and mause_click:
            if b["img"] == porta_b_img:
                b["img"] = porta_b2_img
                for outro in mund:
                    if (outro["rect"].x == b["rect"].x and
                        outro["rect"].y == b["rect"].y - 75):
                        outro["img"] = porta_c2_img
                sleep(tenp)
            elif b["img"] == porta_c_img:
                b["img"] = porta_c2_img
                for outro in mund:
                    if (outro["rect"].x == b["rect"].x and
                        outro["rect"].y == b["rect"].y +75):
                        outro["img"] = porta_b2_img
                sleep(tenp)
            elif b["img"] == porta_b2_img:
                b["img"] = porta_b_img
                for outro in mund:
                    if (outro["rect"].x == b["rect"].x and
                        outro["rect"].y == b["rect"].y - 75):
                        outro["img"] = porta_c_img
                sleep(tenp)
            elif b["img"] == porta_c2_img:
                b["img"] = porta_c_img
                for outro in mund:
                    if (outro["rect"].x == b["rect"].x and
                        outro["rect"].y == b["rect"].y +75):
                        outro["img"] = porta_b_img
                sleep(tenp)
    
    #--------- GRAVIDADE ---------
    no_chao = False

    for lista in [mund, chao_grama, chao_pedra, chao_pedra2]:
        for b in blocos_proximos(player, lista):    
            if lista == chao_pedra:
                if player.colliderect(b["rect"]):
                        no_chao = True
                        player.bottom = b["rect"].top + 1
                        v = 0
                        break
            elif lista == mund:
                if b["img"] != ceu_img and b["img"] != porta_b2_img and b["img"] != porta_c2_img:
                    if player.colliderect(b["rect"]):
                        no_chao = True
                        player.bottom = b["rect"].top + 1
                        v = 0
                        break
            elif player.colliderect(b):
                no_chao = True
                player.bottom = b.top + 1
                v = 0
                break
        if no_chao:
            break

    if not no_chao:
        if v <= 50:
            v += 0.7
            player.y += v
        else:
            player.y += v
        
    #---------- QUEBRAR -----------
    if btn_que.collidepoint(mause_pos) and mause_click:
        if l == True:
            l = False
            btq = vermelho
            sleep(tenp)
        elif l == False:
            l = True
            btq = verde
            sleep(tenp)
    if l == True:
        if mause_click:
            for lista in [mund, chao_grama, chao_pedra]:
                for b in blocos_proximos(player, lista):
                    if lista == chao_pedra:
                        if b["rect"].collidepoint(mause_pos2):
                            lista.remove(b)
                            if b["img"] == carvao_img:
                                p_x = b["rect"].x
                                p_y = b["rect"].y
                                carvoes.append(Carvao(p_x, p_y, carvao_item_img))
                            if b["img"] == ferro_img:
                                p_x = b["rect"].x
                                p_y = b["rect"].y
                                ferros.append(Ferro(p_x, p_y, ferro_item_img))
                            mapa.fill((0,0,0,0))
                            if lista == chao_grama:
                                bloc_gram += 1
                            if lista == chao_pedra:
                                bloc_pedr += 1
                            for b in chao_grama:
                                mapa.blit(grama_img, b)
                            for b in chao_pedra:
                                mapa.blit(b["img"], b["rect"])
                    elif lista == mund:
                        if b["img"] != ceu_img:
                            if b["rect"].collidepoint(mause_pos2):
                                if b["img"] == grama_img:
                                    bloc_gram += 1
                                if b["img"] == pedra_img:
                                    bloc_pedr += 1
                                if b["img"] == madeira_img:
                                    bloc_made += 1
                                if b["img"] == porta_b_img or b["img"] == porta_b2_img:
                                    bloc_port += 1
                                    for outro in mund:
                                        if (outro["rect"].x == b["rect"].x and
                                            outro["rect"].y == b["rect"].y - 75):
                                            outro["img"] = ceu_img
                                if b["img"] == porta_c_img or b["img"] == porta_c2_img:
                                    bloc_port += 1
                                    for outro in mund:
                                        if (outro["rect"].x == b["rect"].x and
                                            outro["rect"].y == b["rect"].y + 75):
                                            outro["img"] = ceu_img
                                b["img"] = ceu_img
                    elif b.collidepoint(mause_pos2):
                        lista.remove(b)
                        mapa.fill((0,0,0,0))
                        if lista == chao_grama:
                            bloc_gram += 1
                        if lista == chao_pedra:
                            bloc_pedr += 1
                        for b in chao_grama:
                            mapa.blit(grama_img, b)
                        for b in chao_pedra:
                            mapa.blit(b["img"], b["rect"])
                        
    # ------------ CONSTRUIR ----------------
    if btn_que2.collidepoint(mause_pos) and mause_click:
        if l2 == True:
            l2 = False
            btq2 = vermelho
            sleep(tenp)
        elif l2 == False:
            l2 = True
            btq2 = verde
            sleep(tenp)
    if l2 == True:
        if mause_click:
            block = mause_pos
                        
    if block != None:
        for b in blocos_proximos(player, mund):
            if b["rect"].collidepoint(mause_pos2):

                if tip_constr == "grama" and b["img"] == ceu_img:
                    if bloc_gram >= 1:
                        bloc_gram -= 1
                        b["img"] = bloc_constr

                elif tip_constr == "pedra" and b["img"] == ceu_img:
                    if bloc_pedr >= 1:
                        bloc_pedr -= 1
                        b["img"] = bloc_constr

                elif tip_constr == "madeira" and b["img"] == ceu_img:
                    if bloc_made >= 1:
                        bloc_made -= 1
                        b["img"] = bloc_constr
                
                elif tip_constr == "taboa" and b["img"] == ceu_img:
                    if bloc_tabo >= 1:
                        bloc_tabo -= 1
                        b["img"] = bloc_constr
                
                elif tip_constr == "porta" and b["img"] == ceu_img:
                    if bloc_port >= 1:
                        bloc_port -= 1
                        b["img"] = bloc_constr
                        for outro in mund:
                            if (outro["rect"].x == b["rect"].x and
                                outro["rect"].y == b["rect"].y - 75):
                                outro["img"] = porta_c_img
                                sleep(tenp)

                block = None
                break
    for mb in mobs:
        if mb.perto_do_player(player):
            mb.mov()
            mb.gravidade(mund, chao_grama, chao_pedra, chao_pedra2)
            mb.most(tela, camera_x, camera_y)
            t += 1/fps
            if t >= 1:
                mb.sort()
                t = 0
    ws = randint(0, 50)
    #ws = 5
    if ws == 5:
        mobs.append(mob(vaca_img))
    pygame.display.update()
