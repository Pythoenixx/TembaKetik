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
cyan = 'cyan'

# Generate some random data points
n = 10 # Number of points
max_data = 690
data = [random.randint(0, max_data) for _ in range(n)] # Y values
ceiling_data = 10 * round(max(data)/10)
print(data) # Print the data for reference

# Plot the data points and connect them with lines
point_radius = 5
line_width = 2

# Set up margins and axes
margin = 75
x_axis = (margin, height - margin, width - margin, height - margin)
y_axis = (margin, height - margin, margin, margin)

tick_size = 5
tick_font = pygame.font.SysFont("Arial", 15)
bil_penanda_aras = 4
hx = margin + 10 * (width - 2 * margin) / 10
hy = height - margin
for i in range(bil_penanda_aras + 1): #sbb start dari 0 so kene 11 bkn 10
    # Draw vertical ticks and labels
    vx = margin
    vy = height - margin - i * (height - 2 * margin) / bil_penanda_aras
    label_value = int(i * ceiling_data / bil_penanda_aras)
    tick_label = tick_font.render(str(label_value), True, 'lime')
    screen.blit(tick_label, (vx - 30, vy - 5))
    pygame.draw.line(screen, 'orange', (margin, vy), (hx, vy))

pygame.draw.line(screen, 'orange', (margin, height - margin), (hx, hy))

for i in range(n):
    # Convert the data point to screen coordinates
    x = margin + i * (width - 2 * margin) / (n - 1)
    y = height - margin - data[i] * (height - 2 * margin) / ceiling_data
    # Draw the point as a blue circle
    pygame.draw.circle(screen, cyan, (x, y), point_radius)
    # Draw the line segment as a red line
    if i > 0:
        # Get the previous point's coordinates
        prev_x = margin + (i - 1) * (width - 2 * margin) / (n - 1)
        prev_y = height - margin - data[i - 1] * (height - 2 * margin) / ceiling_data
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
