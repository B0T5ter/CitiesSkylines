import pygame
pygame.init()

# Ustawienia okna
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Ustawienia kwadratu
square_size = 100
square_color = (255, 255, 255, 128)  # Kolor biały z przezroczystością (128 to półprzezroczystość)
square_surface = pygame.Surface((square_size, square_size), pygame.SRCALPHA)  # Tworzymy powierzchnię z przezroczystością
square_surface.fill(square_color)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Wypełniamy tło na szaro
    screen.fill((100, 100, 100))

    # Rysowanie losowego tła lub elementów, które mają być "rozmazane"
    pygame.draw.circle(screen, (0, 255, 0), (400, 300), 150)
    pygame.draw.circle(screen, (255, 0, 0), (300, 200), 100)
    
    # Rysowanie półprzezroczystego kwadratu
    screen.blit(square_surface, (350, 250))  # Rysowanie na środku ekranu

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
