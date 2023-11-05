import pygame,sys,random
from pemalar import *
#klo penembak nya kat tgh pun agak interesting
# Initialize pygame
pygame.init()

# Create a window object
screen = pygame.display.set_mode((WN_LEBAR, WN_TINGGI))
clock = pygame.time.Clock()
# Set the title of the window
pygame.display.set_caption("Shootype")

class Latar:
    def __init__(self, x, y, veloX, veloY) -> None:
        self.x = x
        self.y = y
        self.veloX = veloX
        self.veloY = veloY
latar_x,latar_y = 0,WN_TINGGI
latar = pygame.image.load('img/angkasa1.png').convert_alpha()

latar = pygame.transform.scale(latar,(WN_LEBAR*10,WN_TINGGI*10))


# Get the center of the screen
center_x = screen.get_width() // 2
center_y = screen.get_height() // 2

# Draw a horizontal line in the center of the screen
pygame.draw.line(screen, (255, 255, 255), (center_x - 100, center_y), (center_x + 100, center_y), 5)

# Create a rectangle object with a position of (50, 50) and a size of (100, 100)
rect = pygame.Rect(0, 0, 40, 40)
rect.center = (center_x, WN_TINGGI - 100)

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
            
    kotak_latar = latar.get_rect(midbottom=(latar_x,latar_y))
    screen.fill((0, 0, 0))
    screen.blit(latar, kotak_latar)
    
    latar_y += 1
    # Check if the image goes off the bottom of the screen
    if latar_y > (latar.get_height()):
        # Wrap the image around to the top of the screen
        latar_y -= latar.get_height() - WN_TINGGI
        latar_x += 100
        if latar_x > (latar.get_width()):
            latar_x = random.randint(0,latar.get_width())
    
    print("coord Y",latar_y)
    # print(latar.get_size()) (5000, 8200)
    
    # Draw a red square on the screen using the rectangle object
    pygame.draw.rect(screen, (255, 0, 0), rect)
    
    pygame.display.flip()
    clock.tick(FPS)
