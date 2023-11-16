import pygame,sys,random
from scripts.pemalar import *
from scripts.latar import Latar
from scripts.musuh import Musuh,jana_musuh
import random
#klo penembak nya kat tgh pun agak interesting
# Initialize pygame
pygame.init()

# Create a window object
screen = pygame.display.set_mode((WN_LEBAR, WN_TINGGI))
clock = pygame.time.Clock()
# Set the title of the window
pygame.display.set_caption("TembaKetik")

# Get the center of the screen
center_x = screen.get_width() // 2
center_y = screen.get_height() // 2

# Draw a horizontal line in the center of the screen
pygame.draw.line(screen, (255, 255, 255), (center_x - 100, center_y), (center_x + 100, center_y), 5)

# Create a rectangle object with a position of (50, 50) and a size of (100, 100)
pemain_rect = pygame.Rect(0, 0, 40, 40)
pemain_rect.center = (center_x, WN_TINGGI - 100)

group_musuh = jana_musuh(10, WN_LEBAR, pemain_rect)

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
    
    # Draw a red square on the screen using the rectangle object
    pygame.draw.rect(screen, (255, 0, 0), pemain_rect)
    
    group_musuh.draw(screen)
    group_musuh.update(WN_TINGGI)
    
    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.set_caption(f'{clock.get_fps() :.1f}')