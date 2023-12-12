import pygame,sys
from scripts.pemalar import *
from scripts.latar import Latar
from scripts.musuh import jana_ombak, assets_load
from scripts.pemain import Pemain

#klo penembak nya kat tgh pun agak interesting
# Initialize pygame
pygame.init()

# Create a window object
icon = pygame.image.load('img/kapal_angkasa.PNG')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WN_LEBAR, WN_TINGGI))

clock = pygame.time.Clock()
char_typed = ''
char_updated = False
font = pygame.font.SysFont("Arial", 20)

assets = {
    'Tiny_Kamikaze' : assets_load('img/tiny_kamikaze_ship.png',50),
    'Kamikaze' : assets_load('img/kamikaze_ship.png',50),
}


# Get the center of the screen
center_x = screen.get_width() // 2
center_y = screen.get_height() // 2

pemain = Pemain(center_x, WN_TINGGI - 100, 'img/player_ship.PNG')
group_pemain = pygame.sprite.Group()
group_pemain.add(pemain)

group_musuh = pygame.sprite.LayeredUpdates()
jana_ombak(group_musuh, assets, WN_LEBAR, pemain.rect, font)

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                char_typed = char_typed[:-1]  #amik smua value selain akhir sekali dlm list tu
            else:
                char_typed += event.unicode
                char_updated = True
            
    
    #biar x de trail
    screen.fill((0, 0, 0))
    latar.gerak(screen)
    
    text = font.render(char_typed, True, (255, 255, 255), (0, 0, 0))
    screen.blit(text, (0, 0))
    
    group_pemain.draw(screen) #try cari group sprite utk yg ada 1 sprite je
    group_pemain.update(screen, group_musuh, char_typed, char_updated)
    char_updated = False
    
    group_musuh.draw(screen)
    group_musuh.update(screen, WN_TINGGI, group_musuh)
    
    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.set_caption(f'TembaKetik FPS: {clock.get_fps() :.1f}')# f' ' tu utk tukar jdi f-string (mcm string data type)

