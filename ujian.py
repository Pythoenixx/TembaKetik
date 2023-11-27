import pygame

# Initialize pygame
pygame.init()

# Create a screen surface with a size of 800 by 600 pixels
screen = pygame.display.set_mode((800, 600))

# Fill the screen with black color
screen.fill((0, 0, 0))

# Create a font object
font = pygame.font.SysFont("Arial", 64)

# Create a text surface object
text = font.render("Hello, Pygame!", True, (255, 0, 0), (0, 0, 255))

# Create a rectangular object for the text surface object
text_rect = text.get_rect()

# Set the center of the rectangular object
text_rect.center = (400, 300)



# Create a game loop
running = True
while running:
    # Get a list of events
    events = pygame.event.get()
    # Loop through the events
    for event in events:
        # Check if the user has clicked the close button
        if event.type == pygame.QUIT:
            # Exit the loop and quit the program
            running = False
            pygame.quit()
    screen.blit(text, text_rect)