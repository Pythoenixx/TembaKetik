import pygame

# Initialize pygame
pygame.init()

# Create a screen surface with a size of 800 by 600 pixels
screen = pygame.display.set_mode((800, 600))

# Fill the screen with black color
screen.fill((0, 0, 0))

image = pygame.image.load('img/tahi_bintang.png').convert_alpha()
mask = pygame.mask.from_surface(image)
outline_points = mask.outline()
# Get the bottom left rectangle and its coordinates
bottom_left_point = outline_points[1]
bottom_left_x = bottom_left_point[0]
bottom_left_y = bottom_left_point[1]
# Sort the list by y-values in descending order
outline_points.sort (key=lambda c: c [1], reverse=True)

# Find the minimum x-value among the coordinates with the highest y-value
min_x = min(c[0] for c in outline_points if c [1] == outline_points [0][1])
print(outline_points[0][1])

# Return the coordinate that has both the highest y-value and the minimum x-value
bottom_left = next(c for c in outline_points if c [0] == min_x and c [1] == outline_points [0][1])

clock = pygame.time.Clock()
FPS = 60
i = 0
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
    screen.blit(image, (0, 0))
    # i += 1
    # if i == len(outline_points):
    #     i = 0
    # print(i,len(outline_points))
    
    
    # pygame.draw.circle(screen, (255, 0, 0), outline_points[len(outline_points)//2], 1)
    # pygame.draw.circle(screen, (255, 0, 0), outline_points[len(outline_points)*3//4], 1)
    pygame.draw.circle(screen, (255, 255, 255), bottom_left, 1)
    clock.tick(FPS)
    pygame.display.flip()