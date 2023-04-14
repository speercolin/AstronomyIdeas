# Importing pygame and math libraries
import pygame
import math

# Initialize Pygame
pygame.init()

# Create the screen dimensions
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Calculate center of the screen
center_x = screen_width // 2
center_y = screen_height // 2
center = (center_x, center_y)

# Loading space background to the screen
space_background = pygame.image.load("space_background.jpg")

# Defining the Sun
sun_radius = 100

# Defining Mercury + speed
mercury_radius = 10
mercury_angle = 0
mercury_animation_speed = 0.1

# Defining Venus + speed
venus_radius = 15
venus_angle = 0
venus_animation_speed = 0.05

# Window loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating the space background image
    screen.blit(space_background, (0, 0))

    # Drawing the Sun
    pygame.draw.circle(screen, (253, 184, 19), (center_x, center_y), sun_radius)
    pygame.display.flip()

    # Creating the path of Mercury
    mercury_angle += mercury_animation_speed
    mercury_x = center[0] + (sun_radius + 50) * math.cos(mercury_angle * math.pi / 180)
    mercury_y = center[1] + (sun_radius + 50) * math.sin(mercury_angle * math.pi / 180)
    mercury_center = (int(mercury_x), int(mercury_y))

    # Drawing Mercury
    pygame.draw.circle(screen, (140, 140, 148), mercury_center, mercury_radius)
    pygame.display.flip()

    # Creating the path of Venus
    venus_angle += venus_animation_speed
    venus_x = center[0] + (sun_radius + 100) * math.cos(venus_angle * math.pi / 180)
    venus_y = center[1] + (sun_radius + 100) * math.sin(venus_angle * math.pi / 180)
    venus_center = (int(venus_x), int(venus_y))

    # Drawing Venus
    pygame.draw.circle(screen, (193, 143, 23), venus_center, venus_radius)
    pygame.display.flip()

pygame.quit()
