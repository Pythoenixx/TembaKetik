import pygame
import sys
from pemalar import *
#klo penembak nya kat tgh pun agak interesting
# Initialize pygame
pygame.init()

# Create a window object
screen = pygame.display.set_mode((WN_LEBAR, WN_TINGGI))
clock = pygame.time.Clock()
# Set the title of the window
pygame.display.set_caption("Shootype")

latar = pygame.image.load('img/angkasa1.png').convert_alpha()
latar = pygame.transform.scale(latar,(WN_LEBAR*10,WN_TINGGI*10))
latar_x,latar_y = 0,0


# Get the center of the screen
center_x = screen.get_width() // 2
center_y = screen.get_height() // 2

# Draw a horizontal line in the center of the screen
pygame.draw.line(screen, (255, 255, 255), (center_x - 100, center_y), (center_x + 100, center_y), 5)

# Create a rectangle object with a position of (50, 50) and a size of (100, 100)
rect = pygame.Rect(0, 0, 40, 40)
rect.center = (center_x, WN_TINGGI - 100)

# Draw a red square on the screen using the rectangle object
pygame.draw.rect(screen, (255, 0, 0), rect)

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
    latar_x -= 0
    latar_y += 1
    screen.fill((0, 0, 0))
    screen.blit(latar, (latar_x,latar_y))
    
    pygame.display.flip()
    clock.tick(FPS)
