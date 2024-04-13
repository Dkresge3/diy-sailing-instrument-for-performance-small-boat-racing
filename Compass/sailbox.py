import pygame
import sys
from berryIMU import *

# Initialize the IMU sensor
imu = BerryIMU()

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (width, height)
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Compass Heading")

# Loop until the user clicks the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    heading = imu.get_compass_data()

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render("Heading: " + str(heading), 1, (10, 10, 10))
    screen.blit(text, (50,50))

    # --- Go ahead and update the screen with what we've drawn
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit
pygame.quit()