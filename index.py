import pygame
import random
import math

#Okienko
windowHeight = 800  
windowWidth = 1000
screen = pygame.display.set_mode((windowWidth,windowHeight))
CLOCK = pygame.time.Clock()
pygame.font.init()
#Zmienne
money = 10000
wybrana = None
cenaDrogi = 100
cenaDomu = 300
cenaSklepu = 600
cenaPracy = 1500
startowi_ludzie = 10
maks_dom = 4
maks_sklep = 8
maks_praca = 12
cenaParku = 2000

nowi_ludzie_przedzial = (100, 100)
szukanie_miejsca_przedzial = (1,1)
dlugosc_w_domu = (1,5)
dlugosc_w_pracy = (1,10)
dlugosc_w_sklepie = (1,6)

#Obrazy
trawaPng = pygame.image.load("img/trawa.png")
pointerImg = pygame.image.load("img/pointer.png").convert_alpha()
noRoadIcon = pygame.image.load("img\\noRoadIcon.png").convert_alpha()

roadIconPng = pygame.image.load("img\\roadicon.png")
roadIconChoosenImg = pygame.image.load("img\\roadiconchoosen.png")
roadIconLowImg = pygame.image.load("img\\roadiconlow.png")
roadImg = pygame.image.load("img\\road.png")

houseIconChoosenImg = pygame.image.load("img\houseIconchoosen.png")
houseIconLowImg = pygame.image.load("img\houseIconlow.png")
houseIconImg = pygame.image.load("img\houseIcon.png")
houseImg = pygame.image.load("img\house.png")

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
#Powierzchnia
class Powierzchnia:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.lenght = 50
        self.img = trawaPng
        self.stan = 'grass'
        self.ludnosc = 0
        self.isRoad = False

    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        self.isRoad = False
        if self.stan == "park" or self.stan == "work" or self.stan == 'shop' or self.stan == 'house': 
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
        if wybrana == "road" and money >= cenaDrogi and self.stan == 'grass':
            self.img = roadImg
            self.stan = 'road'
            money -= cenaDrogi
        if wybrana == "house" and money >= cenaDomu and self.stan == 'grass':
            self.img = houseImg
            self.stan = 'house'
            money -= cenaDomu
        if wybrana == "shop" and money >= cenaSklepu and self.stan == 'grass':
            self.img = shopImg
            self.stan = 'shop'
            money -= cenaSklepu
        if wybrana == "work" and money >= cenaPracy and self.stan == 'grass':
            self.img = workImg
            self.stan = 'work'
            money -= cenaPracy
        if wybrana == "park" and money >= cenaParku and self.stan == 'grass':
            self.img = parkImg
            self.stan = 'park'
            money -= cenaParku
    def wypisanie_ilosci(self):
        if self.stan != "grass" and self.stan != "park" and self.stan != 'road' and self.isRoad == True:
            fontLudnosc = pygame.font.Font('Oswald-VariableFont_wght.ttf', 20)
            cena = fontLudnosc.render(f'{self.ludnosc}', True, (0, 0, 0))
            screen.blit(cena, (x.x + 20, x.y + 10))

# Tworzenie ludzi
class Czlowiek:
    def __init__(self, dom = None, praca = None, sklep = None, rozrywka = None, szczescie = 0):
        self.dom = dom
        self.praca = praca
        self.sklep = sklep
        self.rozrywka = rozrywka
        self.szczescie = szczescie
        self.timer = random.randint(*szukanie_miejsca_przedzial) * 60
        self.x = None
        self.y = None
        self.gotowy = False
        self.kolor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    
    def szukanie(self):
        if self.timer > 0:
            self.timer -= 1
        if self.timer == 0:
            self.timer = random.randint(*szukanie_miejsca_przedzial) * 60
            for x in zbiorPowierzchni:
                if self.dom == None and x.stan == 'house' and x.ludnosc < maks_dom and x.isRoad == True:
                    self.dom = (x.x//50, x.y//50)
                    x.ludnosc += 1
                    self.x = x.x//50
                    self.y = x.y//50
        
                if self.sklep == None and x.stan == 'shop' and x.ludnosc < maks_sklep and x.isRoad == True:
                    self.sklep = (x.x//50, x.y//50)
                    x.ludnosc += 1
                if self.praca == None and x.stan == 'work' and x.ludnosc < maks_praca and x.isRoad == True:
                    self.praca = (x.x//50, x.y//50)
                    x.ludnosc += 1
                
        self.szczescie = 0
        if self.dom != None:
            self.szczescie += 25
            for x in zbiorPowierzchni:
                if x.stan == "park":
                    d = math.sqrt((self.dom[0] - x.x)**2 + (self.dom[1] - x.y)**2)
                    if d <= 200:
                        self.szczescie += 25
                        break
        if self.praca != None:
            self.szczescie += 25
        if self.sklep != None:
            self.szczescie += 25
        if self.praca != None and self.dom != None and self.sklep != None:
            self.gotowy = True
            self.miejsce = 'house'
          

    def dokonywanie_wyboru(self):
        if self.gotowy:
            self.droga = szukanie_drogi(self.dom, self.praca)
            print(self.droga)

    def dane(self):
        print("Timer miejsca", self.timerMiejsca)
        print("obecne miejsce", self.miejsce)
        print("cel", self.cel)
        
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
    return zapotrzebowanie_dom, zapotrzebowanie_praca, zapotrzebowanie_sklep, srednie_szczescie

#Szukanie drogi
def szukanie_drogi(start, end):
    linia = []
    for x in zbiorPowierzchni:
        if x.stan != "grass":
            linia.append(0)
        else:
            linia.append(1)
    segment_size = windowWidth//50
    maze = [linia[i:i + segment_size] for i in range(0, len(linia), segment_size)]
    print(maze)
    rows, cols = len(maze), len(maze[0])
    queue = [start]            # Kolejka jako lista z punktem początkowym
    visited = {tuple(start): None}  # Słownik śledzący odwiedzone komórki i ścieżkę

    while queue:
        current = queue.pop(0)  # Usuwamy pierwszy element z kolejki (FIFO)

        if current == end:
            # Rekonstrukcja ścieżki
            path = []
            while current:
                path.append(current)
                current = visited[tuple(current)]
            return path[::-1]  # Zwracamy ścieżkę od startu do końca

        # Przeszukiwanie sąsiadów: góra, dół, lewo, prawo
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            row, col = current[0] + dr, current[1] + dc

            if 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0:  # 0 = wolna komórka, 1 = ściana
                neighbor = [row, col]
                if tuple(neighbor) not in visited:  # Sprawdzenie, czy nieodwiedzony
                    visited[tuple(neighbor)] = current  # Zapisujemy, skąd przyszliśmy
                    queue.append(neighbor)            # Dodajemy sąsiada do kolejki

    return None  # Zwracamy None, jeśli brak ścieżki do celu
#Tworzenie powierzchni początkowej
zbiorPowierzchni = []
for y in range(3, (windowHeight-100)//50):
    for x in range(windowWidth//50):
        zbiorPowierzchni.append(Powierzchnia(x*50, y*50))

class Pointer:
    def __init__(self):
        self.img = pointerImg

    def repositionPointer(self):
        self.x, self.y = pygame.mouse.get_pos()
        if self.y >= 150 and self.y <= 700 and self.x >=0 and self.x <= 1000:
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

    def draw(self):
        global wybrana
        if money >= self.cena and wybrana != self.wybor:
            screen.blit(self.img[0], (self.x,self.y))
        elif money < self.cena:
            screen.blit(self.img[2], (self.x,self.y))
        if money >= self.cena and wybrana == self.wybor:
            screen.blit(self.img[1], (self.x,self.y))
        fontCena = pygame.font.Font('Oswald-VariableFont_wght.ttf', 20)
        cena = fontCena.render(f'{self.cena}$', True, (0, 0, 0))
        screen.blit(cena, (self.x + 20, self.y + 20))

    def ifClicked(self):
        global wybrana
        x, y = pygame.mouse.get_pos()
        if x >= self.x and x < self.x + self.lenght and y >= self.y and y < self.y + self.lenght and wybrana != self.wybor:
            wybrana = self.wybor
        elif x >= self.x and x < self.x + self.lenght and y >= self.y and y < self.y + self.lenght and wybrana == self.wybor:
            wybrana = None

ikonkiZbior = [Icons(20, 710, cenaDrogi, (roadIconPng, roadIconChoosenImg, roadIconLowImg), "road"), Icons(120, 710, cenaDomu, (houseIconImg, houseIconChoosenImg, houseIconLowImg), 'house'), Icons(220, 710, cenaSklepu, [shopIconImg, shopIconChoosenImg, shopIconLowImg], 'shop'), Icons(320, 710, cenaPracy, [workIconImg, workIconChoosenImg, workIconLowImg], 'work'), Icons(420, 710, cenaParku, [parkIconImg, parkIconChoosenImg, parkIconLowImg], "park")]
#Wypisywanie tekstow
def wypisywanie_tekstow():
    zapotrzebowanie_dom, zapotrzebowanie_praca, zapotrzebowanie_sklep, srednie_szczescie = sprawdzanie_wartosc_ludzi()
    font = pygame.font.Font('Oswald-VariableFont_wght.ttf', 55)
    #Pieniadze
    ilosc_pieniedzy_text = font.render(f'{money}$', True, (123, 138, 127))
    screen.blit(ilosc_pieniedzy_text, (750, 25))
    #Zapotrzebowanie domy
    zapotrzebowanie_domy_text = font.render(f'{zapotrzebowanie_dom}', True, (0, 153, 0))
    screen.blit(zapotrzebowanie_domy_text, (20, 25))
    #zapotrzebowanie sklep
    zapotrzebowanie_sklep_text = font.render(f'{zapotrzebowanie_sklep}', True, (51, 51, 255))
    screen.blit(zapotrzebowanie_sklep_text, (120, 25))
    #zapotrzebowanie praca
    zapotrzebowanie_praca_text = font.render(f'{zapotrzebowanie_praca}', True, (255, 128, 0))
    screen.blit(zapotrzebowanie_praca_text, (220, 25))
    #Szczescie
    srednie_szczescie_text = font.render(f'{int(srednie_szczescie)}%', True, (255, 0, 255))
    screen.blit(srednie_szczescie_text, (320, 25))

while True:
    screen.fill((30, 125, 60))
    
    for x in zbiorPowierzchni:
        x.draw()
        x.wypisanie_ilosci()
    for x in ikonkiZbior:
        x.draw()
    for x in ludzie:
        x.szukanie()
        x.dokonywanie_wyboru()
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
    wypisywanie_tekstow()
    robienie_ludzi()
    pygame.display.flip()
    CLOCK.tick(30)