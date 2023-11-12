import pygame,sys
from scripts.pemalar import *
from scripts.latar import Latar
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

musuh_rect = pygame.Rect(0, 0, 20, 20)
musuh_rect.center = (20, 100)

musuh_rect2 = pygame.Rect(0, 0, 20, 20)
musuh_rect2.center = (420, -69)

# Define the speed and direction
speed = 0.5
direction = pygame.math.Vector2(pemain_rect.center) - pygame.math.Vector2(musuh_rect.center) # A vector from rect1 to rect2
direction = direction.normalize() # A unit vector with the same direction

# Define the speed and direction
speed2 = 0.8
direction2 = pygame.math.Vector2(pemain_rect.center) - pygame.math.Vector2(musuh_rect2.center) # A vector from rect1 to rect2
direction2 = direction2.normalize() # A unit vector with the same direction

latar = Latar(0, WN_TINGGI, 0, 0.2)
gerakan_x,gerakan_y = musuh_rect.x,musuh_rect.y
gerakan_x2,gerakan_y2 = musuh_rect2.x,musuh_rect2.y
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
    
    gerakan_x +=  (speed * direction.x)
    gerakan_y +=  (speed * direction.y)
    
    # Update the position of rect1
    musuh_rect.x = gerakan_x
    musuh_rect.y = gerakan_y
    
    gerakan_x2 +=  (speed2 * direction2.x)
    gerakan_y2 +=  (speed2 * direction2.y)
    
    # Update the position of rect1
    musuh_rect2.x = gerakan_x2
    musuh_rect2.y = gerakan_y2
    
    
    # print("coord Y",round(latar.y))
    # print(latar.get_size()) (5000, 8200)
    
    # Draw a red square on the screen using the rectangle object
    pygame.draw.rect(screen, (255, 0, 0), pemain_rect)
    pygame.draw.rect(screen, (255, 255, 0), musuh_rect)
    pygame.draw.rect(screen, (0, 255, 0), musuh_rect2)
    
    pygame.display.flip()
    clock.tick(FPS)
