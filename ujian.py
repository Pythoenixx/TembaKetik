import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Line Graph with Pygame")

# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Generate some random data points
n = 10 # Number of points
max_data = 690
data = [random.randint(0, max_data) for _ in range(n)] # Y values
print(data) # Print the data for reference

# Plot the data points and connect them with lines
point_radius = 10
line_width = 2

# Set up margins and axes
margin = 75
x_axis = (margin, height - margin, width - margin, height - margin)
y_axis = (margin, height - margin, margin, margin)

# Set up labels and ticks
font = pygame.font.SysFont("Arial", 20)
x_label = font.render("X", True, green)
y_label = font.render("Y", True, white)
screen.blit(x_label, (width - margin + 10, height - margin - 10))
screen.blit(y_label, (margin - 10, margin - 20))
tick_size = 5
tick_font = pygame.font.SysFont("Arial", 15)
for i in range(11): #sbb start dari 0 so kene 11 bkn 10
    # Draw horizontal ticks and labels
    hx = margin + i * (width - 2 * margin) / 10
    hy = height - margin
    pygame.draw.line(screen, 'orange', (hx, hy), (hx, hy + tick_size))
    tick_label = tick_font.render(str(i), True, 'orange')
    screen.blit(tick_label, (hx - 5, hy + 10))
    # Draw vertical ticks and labels
    vx = margin
    vy = height - margin - i * (height - 2 * margin) / 10
    pygame.draw.line(screen, 'lime', (vx, vy), (vx - tick_size, vy))
    tick_label = tick_font.render(str(int(i * max_data/10)), True, 'lime')
    screen.blit(tick_label, (vx - 20, vy - 5))

pygame.draw.line(screen, 'orange', (margin, height - margin), (hx, hy))
pygame.draw.line(screen, 'lime', (margin, height - margin), (vx, vy))

for i in range(n):
    # Convert the data point to screen coordinates
    x = margin + i * (width - 2 * margin) / (n - 1)
    y = height - margin - data[i] * (height - 2 * margin) / max_data
    # Draw the point as a blue circle
    pygame.draw.circle(screen, blue, (x, y), point_radius)
    # Draw the line segment as a red line
    if i > 0:
        # Get the previous point's coordinates
        prev_x = margin + (i - 1) * (width - 2 * margin) / (n - 1)
        prev_y = height - margin - data[i - 1] * (height - 2 * margin) / max_data
        # Draw the line from the previous point to the current point
        pygame.draw.line(screen, red, (prev_x, prev_y), (x, y), line_width)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
