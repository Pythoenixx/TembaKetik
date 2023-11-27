import pygame,sys
from scripts.pemalar import *
from scripts.latar import Latar
from scripts.entities import jana_musuh, Pemain

#klo penembak nya kat tgh pun agak interesting
# Initialize pygame
pygame.init()

# Create a window object
icon = pygame.image.load('img/kapal_angkasa.PNG')#gmbr ni bgi libpng warning: iCCP: known incorrect sRGB profile?
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WN_LEBAR, WN_TINGGI))
clock = pygame.time.Clock()

# Get the center of the screen
center_x = screen.get_width() // 2
center_y = screen.get_height() // 2

# Draw a horizontal line in the center of the screen
pygame.draw.line(screen, (255, 255, 255), (center_x - 100, center_y), (center_x + 100, center_y), 5)

# Create a rectangle object with a position of (50, 50) and a size of (100, 100)
pemain_rect = pygame.Rect(0, 0, 40, 40)
pemain_rect.center = (center_x, WN_TINGGI - 100)

pemain = Pemain(center_x, WN_TINGGI - 100, 'img/kapal_angkasa.PNG')
group_pemain = pygame.sprite.Group()
group_pemain.add(pemain)

group_musuh = jana_musuh(10, WN_LEBAR, pemain.rect, pygame.font.SysFont("Tahoma", 20))#bukan patut tinggi ke?

latar = Latar(0, WN_TINGGI, 0, 0.2)
# Create a game loop
running = True
while running:
    # Get a list of events
    events = pygame.event.get()
    # Loop through the events
    for event in events:
        # Check if the user has clicked the close button
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            # Exit the loop and quit the program
            running = False
            pygame.quit()
            sys.exit()
        # Check if the mouse has moved
        elif event.type == pygame.MOUSEMOTION:
            # Get the mouse coordinates
            x, y = pygame.mouse.get_pos()
            # Print the mouse coordinates
            print(x, y)
    
    #biar x de trail
    screen.fill((0, 0, 0))
    
    latar.gerak(screen)
    
    # print("coord Y",round(latar.y))
    # print(latar.get_size()) (5000, 8200)
    
    group_pemain.draw(screen)
    
    group_musuh.draw(screen)
    group_musuh.update(screen, WN_TINGGI)
    
    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.set_caption(f'TembaKetik FPS: {clock.get_fps() :.1f}')# f' ' tu utk tukar jdi f-string (mcm string data type)

