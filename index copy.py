import pygame
import random
import math
#from playsound import playsound


#Okienko
windowHeight = 800  
windowWidth = 1000
screen = pygame.display.set_mode((windowWidth,windowHeight))
CLOCK = pygame.time.Clock()
pygame.font.init()
pygame.mixer.init()

#Zmienne
money = 7000000
wybrana = None
cenaDrogi = 100
cenaDomu = 300
cenaSklepu = 600
cenaPracy = 1500
cenaParku = 2000

maks_dom = 4
maks_sklep = 8
maks_praca = 12

minNowiLudzie = 2
maksNowychLudzi = 10
nowi_ludzie_przedzial = (minNowiLudzie, maksNowychLudzi)

dlugosc_w_domu = (1,5)
dlugosc_w_pracy = (2,5)
dlugosc_w_sklepie = (5,10)

godzina = 0
dzien = 1
miesiac = 1
rok = 2000
font_wypisywanie_textow = pygame.font.Font('Oswald-VariableFont_wght.ttf', 55)

budowlane = ['toxicGrass', 'grass']
zabudowane = ['shop', 'house', 'work', 'road']
#Obrazy
pointerImg = pygame.image.load("img/pointer.png").convert_alpha()
noRoadIcon = pygame.image.load("img\\noRoadIcon.png").convert_alpha()
heartIconImg = pygame.image.load("img\heartIcon.png")
peopleIconImg = pygame.image.load("img\peopleIcon.png")
toxicGrassImg = pygame.image.load("img\\toxicGrass.png")

roadIconPng = pygame.image.load("img\\roadicon.png")
roadIconChoosenImg = pygame.image.load("img\\roadiconchoosen.png")
roadIconLowImg = pygame.image.load("img\\roadiconlow.png")
roadImg = pygame.image.load("img\\road.png")

houseIconChoosenImg = pygame.image.load("img\houseIconchoosen.png")
houseIconLowImg = pygame.image.load("img\houseIconlow.png")
houseIconImg = pygame.image.load("img\houseIcon.png")
houseImg = pygame.image.load("img\houses\house1.png").convert_alpha()

workIconChoosenImg = pygame.image.load("img\workIconchoosen.png")
workIconLowImg = pygame.image.load("img\workIconlow.png")
workIconImg = pygame.image.load("img\workIcon.png")
workImg = pygame.image.load("img\work.png")

shopIconChoosenImg = pygame.image.load("img\shopIconchoosen.png")
shopIconLowImg = pygame.image.load("img\shopIconlow.png")
shopIconImg = pygame.image.load("img\shopIcon.png")
shopImg = pygame.image.load("img\shop.png")

parkIconChoosenImg = pygame.image.load("img\parkIconchoosen.png")
parkIconLowImg = pygame.image.load("img\parkIconlow.png")
parkIconImg = pygame.image.load("img\parkIcon.png")
parkImg = pygame.image.load("img\park.png")

housesImgs = [pygame.image.load("img\houses\house1.png"), pygame.image.load("img\houses\house1.png"), pygame.image.load("img\houses\house3.png"), pygame.image.load("img\houses\house4.png"), pygame.image.load("img\houses\house5.png"), pygame.image.load("img\houses\house6.png"), pygame.image.load("img\houses\house7.png"), pygame.image.load("img\houses\house8.png"), pygame.image.load("img\houses\house2.png")]
storesImgS = [pygame.image.load("img\stores\store1.png"), pygame.image.load("img\stores\store1.png"), pygame.image.load("img\stores\store2.png"), pygame.image.load("img\stores\store3.png"), pygame.image.load("img\stores\store4.png"), pygame.image.load("img\stores\store5.png"), pygame.image.load("img\stores\store6.png"), pygame.image.load("img\stores\store7.png"), pygame.image.load("img\stores\store8.png")]
worksImgs = [pygame.image.load("img\works\work1.png"), pygame.image.load("img\works\work2.png"), pygame.image.load("img\works\work3.png"), pygame.image.load("img\works\work4.png"), pygame.image.load("img\works\work5.png"), pygame.image.load("img\works\work6.png"), pygame.image.load("img\works\work7.png"), pygame.image.load("img\works\work8.png")]
grassesimgs = [pygame.image.load("img\grass\grass1.png"), pygame.image.load("img\grass\grass2.png"), pygame.image.load("img\grass\grass3.png"), pygame.image.load("img\grass\grass4.png"), pygame.image.load("img\grass\grass5.png"), pygame.image.load("img\grass\grass6.png"), pygame.image.load("img\grass\grass7.png"), pygame.image.load("img\grass\grass8.png"), pygame.image.load("img\grass\grass9.png"), pygame.image.load("img\grass\grass10.png"), pygame.image.load("img\grass\grass11.png"), ]
parksImgs =[ pygame.image.load("img\parks\park1.png"), pygame.image.load("img\parks\park2.png"), pygame.image.load("img\parks\park3.png"), pygame.image.load("img\parks\park4.png"), pygame.image.load("img\parks\park5.png"), ]


### Drogi
roadgp = pygame.image.load("img\\roads\\raodgp.png")
roadpd = pygame.image.load("img\\roads\\roadpd.png")
roadlg = pygame.image.load("img\\roads\\raodlg.png")
roadld = pygame.image.load("img\\roads\\raodld.png")

roadgd = pygame.image.load("img\\roads\\roadgd.png")
roadlp = pygame.image.load("img\\roads\\roadlp.png")

roadpdl = pygame.image.load("img\\roads\\roadpdl.png")
roadgpl = pygame.image.load("img\\roads\\roadgpl.png")
roaddlg = pygame.image.load("img\\roads\\raoddlg.png")
roadgpd = pygame.image.load("img\\roads\\raodgpd.png")

roadgpld = pygame.image.load("img\\roads\\roadgpdl.png")
###

waterImg = pygame.image.load("img\water\water.png")
#Odglosy
pygame.mixer.music.load('sounds\\background.wav')
pygame.mixer.music.play(-1)

clickWav = pygame.mixer.Sound("sounds\click.wav")
endOfPeriodWav = pygame.mixer.Sound("sounds\endOfperiod.wav")
placingWav = pygame.mixer.Sound("sounds\placing.wav")
#Powierzchnia
class Powierzchnia:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.lenght = 50
        self.stan = 'grass'
        self.ludnosc = 0
        self.isRoad = False
        self.fontLudnosc = pygame.font.Font('Oswald-VariableFont_wght.ttf', 20)
        self.toxic = False
        self.timerZatrucia = 120
        wybor = random.randint(1,30)
        if wybor < 10:
            self.img = grassesimgs[wybor]
        else:
            self.img = grassesimgs[0]

    def draw(self):
        if self.stan == 'water':
          screen.blit(waterImg, (self.x, self.y))  
        else:
            screen.blit(self.img, (self.x, self.y))
            if self.stan == "park" or self.stan == "work" or self.stan == 'shop' or self.stan == 'house' and self.isRoad == False: 
                for x in zbiorPowierzchni:
                    if x.x == self.x and x.y == self.y - 50 and x.stan == 'road':
                        self.isRoad = True
                        break
                    if x.x == self.x + 50 and x.y == self.y and x.stan == 'road':
                        self.isRoad = True
                        break
                    if x.x == self.x and x.y == self.y + 50 and x.stan == 'road':
                        self.isRoad = True
                        break
                    if x.x == self.x - 50 and x.y == self.y and x.stan == 'road':
                        self.isRoad = True
                        break
                if self.isRoad == False:
                    screen.blit(noRoadIcon, (self.x + 10, self.y + 10))

    def budowa(self):
        global wybrana, money
        x, y = pointer.getPointerPosition()
        if self.x != x or self.y != y:
            return
        if wybrana == "road" and money >= cenaDrogi and self.stan in budowlane:
            self.img = roadgpld
            self.stan = 'road'
            money -= cenaDrogi
            placingWav.play()
        if wybrana == "house" and money >= cenaDomu and self.stan in budowlane:
            wybor = random.randint(0,7)
            self.img = housesImgs[wybor]
            self.stan = 'house'
            money -= cenaDomu
            placingWav.play()
        if wybrana == "shop" and money >= cenaSklepu and self.stan in budowlane:
            wybor = random.randint(0,7)
            self.img = storesImgS[wybor]
            self.stan = 'shop'
            money -= cenaSklepu
            placingWav.play()
        if wybrana == "work" and money >= cenaPracy and self.stan in budowlane:
            wybor = random.randint(0,7)
            self.img = worksImgs[wybor]
            self.stan = 'work'
            money -= cenaPracy
            placingWav.play()   
        if wybrana == "park" and money >= cenaParku and self.stan in budowlane:
            wybor = random.randint(0,4)
            self.img = parksImgs[wybor]
            self.stan = 'park'
            money -= cenaParku
            placingWav.play()

    def zatruwanie(self):
        if self.timerZatrucia > 0:
            self.timerZatrucia -= 1
        else:
            self.timerZatrucia = random.randint(1,1)* 60
            wybor = random.randint(1,20)
            for x in zbiorPowierzchni:
                if x.stan == 'grass':
                    if x.x - 50 == self.x and x.y - 50 == self.y and wybor == 1:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x - 50 == self.x and x.y == self.y and wybor == 2:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x - 50 == self.x and x.y + 50 == self.y and wybor == 3:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x + 50 == self.x and x.y - 50 == self.y and wybor == 4:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x + 50 == self.x and x.y + 50 == self.y and wybor == 5:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x == self.x and x.y + 50 == self.y and wybor == 6:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x == self.x and x.y - 50 == self.y and wybor == 7:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x + 50 == self.x and x.y == self.y and wybor == 8:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x - 50 == self.x and x.y - 100 == self.y and wybor == 9:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x == self.x and x.y - 100 == self.y and wybor == 10:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x + 50 == self.x and x.y - 100 == self.y and wybor == 11:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x - 100 == self.x and x.y + 50 == self.y and wybor == 12:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x - 100 == self.x and x.y == self.y and wybor == 13:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x - 100 == self.x and x.y - 50 == self.y and wybor == 14:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x + 100 == self.x and x.y + 50 == self.y and wybor == 15:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x + 100 == self.x and x.y == self.y and wybor == 16:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x + 100 == self.x and x.y - 50 == self.y and wybor == 17:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass'
                        x.toxic = True
                    if x.x - 50 == self.x and x.y + 100 == self.y and wybor == 18:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass' 
                        x.toxic = True
                    if x.x == self.x and x.y + 100 == self.y and wybor == 19:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass' 
                        x.toxic = True
                    if x.x + 50== self.x and x.y + 100 == self.y and wybor == 20:
                        x.img = toxicGrassImg
                        x.stan = 'toxicGrass' 
                        x.toxic = True

                if x.stan == 'house':
                    if x.x - 50 == self.x and x.y - 50 == self.y and wybor == 1:
                        x.toxic = True
                    if x.x - 50 == self.x and x.y == self.y and wybor == 2:
                        x.toxic = True
                    if x.x - 50 == self.x and x.y + 50 == self.y and wybor == 3:
                        x.toxic = True
                    if x.x + 50 == self.x and x.y - 50 == self.y and wybor == 4:
                        x.toxic = True
                    if x.x + 50 == self.x and x.y + 50 == self.y and wybor == 5:
                        x.toxic = True
                    if x.x == self.x and x.y + 50 == self.y and wybor == 6:
                        x.toxic = True
                    if x.x == self.x and x.y - 50 == self.y and wybor == 7:
                        x.toxic = True
                    if x.x + 50 == self.x and x.y == self.y and wybor == 8:
                        x.toxic = True
                    if x.x - 50 == self.x and x.y - 100 == self.y and wybor == 9:
                        x.toxic = True
                    if x.x == self.x and x.y - 100 == self.y and wybor == 10:
                        x.toxic = True
                    if x.x + 50 == self.x and x.y - 100 == self.y and wybor == 11:
                       x.toxic = True
                    if x.x - 100 == self.x and x.y + 50 == self.y and wybor == 12:
                        x.toxic = True
                    if x.x - 100 == self.x and x.y == self.y and wybor == 13:
                        x.toxic = True
                    if x.x - 100 == self.x and x.y - 50 == self.y and wybor == 14:
                        x.toxic = True
                    if x.x + 100 == self.x and x.y + 50 == self.y and wybor == 15:
                       x.toxic = True
                    if x.x + 100 == self.x and x.y == self.y and wybor == 16:
                        x.toxic = True
                    if x.x + 100 == self.x and x.y - 50 == self.y and wybor == 17:
                        x.toxic = True
                    if x.x - 50 == self.x and x.y + 100 == self.y and wybor == 18:
                       x.toxic = True
                    if x.x == self.x and x.y + 100 == self.y and wybor == 19:
                        x.toxic = True
                    if x.x + 50== self.x and x.y + 100 == self.y and wybor == 20:
                        x.toxic = True

    def wypisanie_ilosci(self):
        if self.stan != "grass" and self.stan != "park" and self.stan != 'road' and self.isRoad == True:
            ludnosc_text = self.fontLudnosc.render(f'{self.ludnosc}', True, (255, 255, 255))
            screen.blit(ludnosc_text, (x.x + 20, x.y - 5))

    def ksztaltowanie_drogi(self):
        if self.stan != 'road':
            return
        
        gora = False
        prawo = False
        lewo = False
        dol = False
        #print(self.x , self.x)
        for x in zbiorPowierzchni:
            if self.x == x.x - 50 and self.y == x.y and x.stan == "road":
                lewo = True
            if self.x == x.x + 50 and self.y == x.y and x.stan == "road":
                prawo = True
            if self.x == x.x and self.y == x.y + 50 and x.stan == "road":
                dol = True
            if self.x == x.x and self.y == x.y - 50 and x.stan == "road":
                gora = True
        #print(prawo, lewo, gora, dol)
        if gora == True and prawo == True and dol == True and lewo == True:
            self.img = roadgpld

        elif gora == True and prawo == True and dol == True:
            self.img = roaddlg
        elif lewo == True and prawo == True and dol == True:
            self.img = roadgpl
        elif gora == True and lewo == True and dol == True:
            self.img = roadgpd
        elif lewo == True and prawo == True and gora == True:
            self.img = roadpdl

        elif prawo == True and lewo == True:
            self.img = roadlp
        elif gora == True and dol == True:
            self.img = roadgd
        
        elif gora == True and prawo == True:
            self.img = roadld#
        elif prawo == True and dol == True:
            self.img = roadlg #
        elif dol == True and lewo == True:
            self.img = roadgp #
        elif lewo == True and gora == True:
            self.img = roadpd

        elif gora == True :
            self.img = roadgd
        elif prawo == True :
            self.img = roadlp
        elif dol == True :
            self.img = roadgd
        elif lewo == True :
            self.img = roadlp
        else:
            self.img = roadgpld

    
    
# Tworzenie ludzi
class Czlowiek:
    def __init__(self, dom = None, praca = None, sklep = None, rozrywka = None, szczescie = 0):
        self.dom = dom
        self.praca = praca
        self.sklep = sklep
        self.rozrywka = rozrywka
        self.szczescie = szczescie
        self.timer = 60
        self.x = None
        self.y = None
        self.gotowy = False
        self.kolor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.step = None
        self.droga = None
        self.cel = None
        self.timerWMiejscu = 100
        self.miejsce = None
        self.wybor = 1
        self.czy_jest_park = False
        self.czy_jest_toksycznie = False

    def szukanie(self):
        if self.timer > 0:
            self.timer -= 1
        else:
            self.timer = 60
            for x in zbiorPowierzchni:
                if self.dom == None and x.stan == 'house' and x.ludnosc < maks_dom and x.isRoad == True:
                    self.dom = [x.x//50, (x.y- 100)//50]
                    x.ludnosc += 1
                    self.x = x.x
                    self.y = x.y
                    self.miejsce = self.dom
                    self.szczescie += 25
                    
                if self.sklep == None and x.stan == 'shop' and x.ludnosc < maks_sklep and x.isRoad == True:
                    self.sklep = [x.x//50, (x.y- 100)//50]
                    x.ludnosc += 1
                    self.szczescie += 25
                if self.praca == None and x.stan == 'work' and x.ludnosc < maks_praca and x.isRoad == True:
                    self.praca = [x.x//50, (x.y- 100)//50]
                    x.ludnosc += 1
                    self.szczescie += 25
        
        d = math.inf
        if self.czy_jest_park == False and self.dom != None:
            for x in zbiorPowierzchni:
                if x.stan == "park":
                    d = math.sqrt(((self.dom[0]* 50)-x.x)**2 + ((self.dom[1] * 50) - x.y)**2)
                if d <= 400:
                    self.czy_jest_park = True
                    self.szczescie += 25
                    break

    def sprawdzenie_toksyczności(self):
        if self.dom != None:
            for x in zbiorPowierzchni:
                if x.toxic == True:
                    if self.dom[0] * 50 == x.x and self.dom[1] * 50 + 100 == x.y:
                        self.szczescie -= 75
                        self.czy_jest_toksycznie = True

    def dokonywanie_wyboru(self):
        if self.praca != None and self.dom != None and self.sklep != None:
            self.gotowy = True
        zarobek = 0
        #print(self.timerWMiejscu)
        if self.gotowy:
            if self.timerWMiejscu < 0:
                self.wybor = random.randint(1,3)
                if self.wybor == 1:
                    self.cel = self.dom
                    self.timerWMiejscu = random.randint(*dlugosc_w_domu) * 60
                if self.wybor == 2:
                    self.cel = self.praca
                    self.timerWMiejscu = random.randint(*dlugosc_w_sklepie) * 60
                if self.wybor == 3:
                    self.cel = self.sklep
                    self.timerWMiejscu = random.randint(*dlugosc_w_pracy) * 60
                self.droga = szukanie_drogi(self.miejsce, self.cel)
                if self.step == None:
                    self.step = 0
                #print(self.droga)
        if self.droga == None:
            self.timerWMiejscu -= 1
        #Wypłata
        if self.timerWMiejscu == 0 and self.wybor == 3:
            zarobek = int(random.randint(1, 50) * (self.szczescie/100))
            zbiorZarobkow.append(TextZarobku(self.x, self.y, zarobek))
        if self.timerWMiejscu == 0 and self.wybor == 2:
            zarobek = int(random.randint(50, 100) * (self.szczescie/100))
            zbiorZarobkow.append(TextZarobku(self.x, self.y, zarobek))
        global money
        money += zarobek
        

    def poruszanie(self):
        if self.droga != None:
            if self.x == self.droga[self.step][0] and self.y == self.droga[self.step][1]:
                self.step += 1
            if self.droga != None:
                if self.step == len(self.droga):
                    self.droga = None
                    self.step = None
                    self.miejsce = self.cel
                    return
            if self.x > self.droga[self.step][0]:
                self.x -= 1
                pygame.draw.circle(screen, self.kolor, (self.x + 40, self.y + 10), 10)
            if self.x < self.droga[self.step][0]:
                self.x += 1
                pygame.draw.circle(screen, self.kolor, (self.x + 10, self.y + 40), 10)
            if self.y > self.droga[self.step][1]:
                self.y -= 1
                pygame.draw.circle(screen, self.kolor, (self.x + 40, self.y + 10), 10)
            if self.y < self.droga[self.step][1]:
                self.y += 1
                pygame.draw.circle(screen, self.kolor, (self.x + 10, self.y + 40), 10)
        
ludzie = [Czlowiek()]
ludzie_timer = random.randint(*nowi_ludzie_przedzial) * 60

def robienie_ludzi():
    global ludzie_timer
    if ludzie_timer == 0:
        ludzie.append(Czlowiek())
        ludzie_timer = random.randint(*nowi_ludzie_przedzial) * 60
    else:
        ludzie_timer -= 1

def sprawdzanie_wartosc_ludzi():
    zapotrzebowanie_dom = 0
    zapotrzebowanie_praca = 0
    zapotrzebowanie_sklep = 0
    srednie_szczescie = 0
    for x in ludzie:
        if x.dom == None:
            zapotrzebowanie_dom += 1
        if x.praca == None:
            zapotrzebowanie_praca += 1
        if x.sklep == None:
            zapotrzebowanie_sklep += 1
        srednie_szczescie += x.szczescie
    srednie_szczescie = srednie_szczescie/len(ludzie)
    if srednie_szczescie < 0:
        srednie_szczescie = 0
    return zapotrzebowanie_dom, zapotrzebowanie_praca, zapotrzebowanie_sklep, srednie_szczescie

#Szukanie drogi
def szukanie_drogi(start, end):
    linia = []
    for x in zbiorPowierzchni:
        if x.stan == "road":
            linia.append(0)
        else:
            linia.append(1)
    
    segment_size = windowWidth//50
    maze = [linia[i:i + segment_size] for i in range(0, len(linia), segment_size)]
    #print('dsadsa', start[1])
    maze[int(start[1])][start[0]] = 0
    maze[end[1]][end[0]] = 0
   
    startx= start[0]
    starty= start[1]
    endx= end[0]
    endy= end[1]
    start = [starty, startx]
    end = [endy, endx]
    rows, cols = len(maze), len(maze[0])
    queue = [start]           
    visited = {tuple(start): None}  

    while queue:
        current = queue.pop(0)  

        if current == end:
            path = []
            while current:
                path.append(current)
                current = visited[tuple(current)]
            odwrotna = path[::-1] 
            path = [] * len(odwrotna)
            for x in range(len(odwrotna)):
                path.append(odwrotna[x][1] * 50)
                path.append((odwrotna[x][0] * 50)+100)
            return [path[i:i + 2] for i in range(0, len(path), 2)]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            row, col = current[0] + dr, current[1] + dc

            if 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0:
                neighbor = [row, col]
                if tuple(neighbor) not in visited: 
                    visited[tuple(neighbor)] = current 
                    queue.append(neighbor)  

    return None 

zbiorPowierzchni = []
for y in range(2, (windowHeight-100)//50):
    for x in range(windowWidth//50):
        zbiorPowierzchni.append(Powierzchnia(x*50, y*50))

class Pointer:
    def __init__(self):
        self.img = pointerImg

    def repositionPointer(self):
        self.x, self.y = pygame.mouse.get_pos()
        if self.y >= 100 and self.y <= 700 and self.x >=0 and self.x <= 1000:
            screen.blit(self.img, (self.x//50 * 50,self.y//50 * 50))

    def getPointerPosition(self):
        x, y = pygame.mouse.get_pos()
        return self.x//50 * 50, self.y//50 * 50
pointer = Pointer()

#Ikonki na dole
class Icons:
    def __init__(self, x, y, cena, img, wybor):
        self.img = img
        self.cena = cena
        self.lenght = 80
        self.x = x
        self.y = y
        self.wybor = wybor
        self.fontCena = pygame.font.Font('Oswald-VariableFont_wght.ttf', 20)
        self.cena_text = self.fontCena.render(f'{self.cena}$', True, (0, 0, 0))
        
    def draw(self):
        global wybrana
        
        if money >= self.cena and wybrana == self.wybor:
            screen.blit(self.img[1], (self.x,self.y))
        if money >= self.cena and wybrana != self.wybor:
            screen.blit(self.img[0], (self.x,self.y))
        elif money < self.cena:
            screen.blit(self.img[2], (self.x,self.y))
        screen.blit(self.cena_text, (self.x + 20, self.y + 20))
        
        

    def ifClicked(self):
        global wybrana
        x, y = pygame.mouse.get_pos()
        if x >= self.x and x < self.x + self.lenght and y >= self.y and y < self.y + self.lenght and wybrana != self.wybor:
            wybrana = self.wybor
            clickWav.play()
        elif x >= self.x and x < self.x + self.lenght and y >= self.y and y < self.y + self.lenght and wybrana == self.wybor:
            wybrana = None
            clickWav.play()
ikonkiZbior = [Icons(20, 710, cenaDrogi, (roadIconPng, roadIconChoosenImg, roadIconLowImg), "road"), Icons(120, 710, cenaDomu, (houseIconImg, houseIconChoosenImg, houseIconLowImg), 'house'), Icons(220, 710, cenaSklepu, [shopIconImg, shopIconChoosenImg, shopIconLowImg], 'shop'), Icons(320, 710, cenaPracy, [workIconImg, workIconChoosenImg, workIconLowImg], 'work'), Icons(420, 710, cenaParku, [parkIconImg, parkIconChoosenImg, parkIconLowImg], "park")]

#Wypisywanie tekstow
def wypisywanie_tekstow(x):
    global money
    zapotrzebowanie_dom, zapotrzebowanie_praca, zapotrzebowanie_sklep, srednie_szczescie = sprawdzanie_wartosc_ludzi()
    font = x
    #Pieniadze
    ilosc_pieniedzy_text = font.render(f'{int(money)}$', True, (255, 255, 255))
    screen.blit(ilosc_pieniedzy_text, (750, 5))
    #Zapotrzebowanie domy
    zapotrzebowanie_domy_text = font.render(f'{zapotrzebowanie_dom}', True, (0, 153, 0))
    screen.blit(zapotrzebowanie_domy_text, (20, 5))
    #zapotrzebowanie sklep
    zapotrzebowanie_sklep_text = font.render(f'{zapotrzebowanie_sklep}', True, (51, 51, 255))
    screen.blit(zapotrzebowanie_sklep_text, (120, 5))
    #zapotrzebowanie praca
    zapotrzebowanie_praca_text = font.render(f'{zapotrzebowanie_praca}', True, (255, 128, 0))
    screen.blit(zapotrzebowanie_praca_text, (220, 5))
    #Szczescie
    srednie_szczescie_text = font.render(f'{int(srednie_szczescie)}', True, (255, 0, 255))
    screen.blit(srednie_szczescie_text, (320, 5))
    screen.blit(heartIconImg,(400, 5))
    #Ludność
    ludnosc_text = font.render(f'{len(ludzie)}', True, (0, 0, 0))
    screen.blit(ludnosc_text, (520, 5))
    screen.blit(peopleIconImg,(610, 5))
    #Data
    global godzina, dzien, miesiac, rok
    godzina += 1
    if godzina == 25:
        godzina = 0
        dzien += 1
        
    if dzien == 31:
        dzien = 1
        miesiac += 1
        zarobek = (len(ludzie) * (random.randint(10,20) + srednie_szczescie))
        money += zarobek
        zbiorZarobkow.append(TextZarobku(780, 700, zarobek))
        endOfPeriodWav.play()
    if miesiac == 13:
        miesiac = 1
        rok += 1
        
    if godzina < 10:
        godzina_text = f'0{godzina}'
    else:
        godzina_text = godzina
    if dzien < 10:
        dzien_text = f'0{dzien}'
    else:
        dzien_text = dzien
    if miesiac < 10:
        miesiac_text = f'0{miesiac}'
    else:
        miesiac_text = miesiac

    data_text = font.render(f'{rok}:{miesiac_text}:{dzien_text}:{godzina_text}', True, (0, 0, 0))
    screen.blit(data_text,(680, 705))

class TextZarobku:
    def __init__(self, x=0, y=0, wartosc=0, wielkosc = 30):
        self.x = x
        self.y = y
        self.wartosc = wartosc
        self.wielkosz = wielkosc 
        self.czas_zycia = 60  # Łączny czas widoczności tekstu w klatkach
        self.alpha = 255  # Początkowa przezroczystość (pełna widoczność)
        self.czas_widoczny = 30  # Liczba klatek, przez które tekst ma być maksymalnie widoczny

        # Inicjalizacja czcionki i renderowanie tekstu
        font_wypisywanie_wartosci = pygame.font.Font('Oswald-VariableFont_wght.ttf', self.wielkosz)
        self.wartosc_text = font_wypisywanie_wartosci.render(f'${self.wartosc}', True, (73, 162, 25))
        self.wartosc_text = self.wartosc_text.convert_alpha()  # Obsługa przezroczystości

    def wypisywanie(self):
        # Aktualizacja pozycji tekstu
        self.y -= 0.5
        self.czas_zycia -= 1

        # Ustawianie przezroczystości po okresie pełnej widoczności
        if self.czas_zycia < self.czas_widoczny:
            self.alpha = max(0, int(255 * (self.czas_zycia / self.czas_widoczny)))
            self.wartosc_text.set_alpha(self.alpha)

        # Rysowanie tekstu na ekranie w nowej pozycji
        text_rect = self.wartosc_text.get_rect(center=(self.x + 25, self.y))
        screen.blit(self.wartosc_text, text_rect)

def wypisywanie_zarobkow():
    for x in zbiorZarobkow:
        x.wypisywanie()
        if x.czas_zycia == 0:
            zbiorZarobkow.pop(0)
kafelkiMenu = []
for y in range(4):
    for x in range(20):
        kafelkiMenu.append(Powierzchnia(x*50, y *50))
for y in range(14, 16):
    for x in range(20):
        kafelkiMenu.append(Powierzchnia(x*50, y *50))

zbiorZarobkow = []
top_blur_rect = pygame.Rect(0, 0, 1000, 100)
bottom_blur_rect = pygame.Rect(0, 700, 1000, 100)
def rysowanie_blurow():
    background_copy = screen.copy()
    blur_surface = pygame.transform.smoothscale(background_copy, (int(screen.get_width() * 0.1), int(screen.get_height() * 0.1)))
    blur_surface = pygame.transform.smoothscale(blur_surface, screen.get_size())
    screen.blit(blur_surface, (0, 0), top_blur_rect)
    screen.blit(blur_surface, (0, 700), bottom_blur_rect) 
    pygame.draw.line(screen, (0, 0, 0), (649, 700), (649,800), 2)

def tworzenie_wody():
        zrobione = 0
        losowa = random.randint(5,13)
        gora = losowa - 1
        if gora < 2:
            gora == 2
        dol = losowa + 1  
        if dol > 16:
            dol == 16
        xx = 0
        poprzednie = (gora + dol)//2
        srodek = (gora + dol)//2
        while zrobione != 20:
            if poprzednie == srodek:
                losowa = random.randint(gora , dol)
            else:
                losowa = srodek
            for x in zbiorPowierzchni:
                if x.x == xx and x.y == losowa * 50:
                    x.stan = 'water'
                    zrobione += 1
                    xx += 50
                    poprzednie = losowa
                    break
        xx = 0
        zapamietanyY = 0
        zrobione = 0
        while zrobione != 20:
            for x in zbiorPowierzchni:
                if x.x == xx and x.stan == 'water':
                    for y in zbiorPowierzchni:
                        if x.x == y.x + 50 and y.stan == 'grass' and y.y != zapamietanyY and x.y == y.y:
                            y.stan = 'water'
                            zapamietanyY = y.y
            xx += 50
            zrobione += 1
            print(xx)
    
        
#tworzenie_wody()
while True:
  
    screen.fill((30, 125, 60))
    maksNowychLudzi = (11 - int(len(ludzie)//10))
    if maksNowychLudzi < 2:
        maksNowychLudzi = 2
        
    czy_maks_szczescia = True
    for x in ludzie:
        if x.szczescie != 100:
            czy_maks_szczescia = False
            break
    if czy_maks_szczescia == True:
        minNowiLudzie = 1
    for x in kafelkiMenu:
        x.draw()
    for x in zbiorPowierzchni:
        x.draw() #
        x.wypisanie_ilosci() #
        x.ksztaltowanie_drogi()
        if x.stan == 'work':
            x.zatruwanie()
    rysowanie_blurow()

    for x in ikonkiZbior:
        x.draw()
    for x in ludzie:
        if x.szczescie != 100:
            x.szukanie()
        x.dokonywanie_wyboru() # 
        if x.czy_jest_toksycznie == False:
            x.sprawdzenie_toksyczności()
        if x.droga != None:
            x.poruszanie() #
        #x.dane()
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for x in zbiorPowierzchni:
                x.budowa()
            for x in ikonkiZbior:
                x.ifClicked()
        if event.type == pygame.QUIT:
           pygame.quit()

    pointer.repositionPointer()
    wypisywanie_tekstow(font_wypisywanie_textow)
    robienie_ludzi()
    if zbiorZarobkow != None:
        wypisywanie_zarobkow()
    pygame.display.update()
    CLOCK.tick(60)
    #print(CLOCK.get_fps())