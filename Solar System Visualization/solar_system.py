# Importing Pygame and math libraries
import pygame
import math

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 1920
screen_height = 1080

# Creating screen + double buffering
screen = pygame.display.set_mode((screen_width, screen_height), pygame.HWSURFACE | pygame.DOUBLEBUF)

# Calculate center of the screen
center_x = screen_width // 2
center_y = screen_height // 2
center = (center_x, center_y)

# Loading space background to the screen
space_background = pygame.image.load("space_background.jpg")

# Defining the Sun
sun_radius = 100

# Defining Mercury & speed
mercury_radius = 10
mercury_angle = 0
mercury_animation_speed = 0.9

# Defining Venus & speed
venus_radius = 15
venus_angle = 0
venus_animation_speed = 0.6

# Defining Earth & speed
earth_radius = 20
earth_angle = 0
earth_animation_speed = 0.4

# Defining our Moon & speed
moon_radius = 5
moon_angle = 0
moon_animation_speed = 1

# Defining Mars & speed
mars_radius = 17.5
mars_angle = 0
mars_animation_speed = 0.2

# Defining Jupiter & speed
jupiter_radius = 35
jupiter_angle = 0
jupiter_animation_speed = 0.09

# Defining Saturn & speed
saturn_radius = 30
saturn_angle = 0
saturn_animation_speed = 0.03

# Defining Saturn's Rings
rings_radius = 40
rings_angle = 0

# Defining Uranus & speed
uranus_radius = 20
uranus_angle = 0
uranus_animation_speed = 0.02

# Defining Neptune & speed
neptune_radius = 25
neptune_angle = 0
neptune_animation_speed = 0.01

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

    # Creating the path of Mercury
    mercury_angle += mercury_animation_speed
    mercury_x = center[0] + (sun_radius + 50) * math.cos(mercury_angle * math.pi / 180)
    mercury_y = center[1] + (sun_radius + 50) * math.sin(mercury_angle * math.pi / 180)
    mercury_center = (int(mercury_x), int(mercury_y))

    # Drawing Mercury
    pygame.draw.circle(screen, (140, 140, 148), mercury_center, mercury_radius)

    # Creating the path of Venus
    venus_angle += venus_animation_speed
    venus_x = center[0] + (sun_radius + 100) * math.cos(venus_angle * math.pi / 180)
    venus_y = center[1] + (sun_radius + 100) * math.sin(venus_angle * math.pi / 180)
    venus_center = (int(venus_x), int(venus_y))

    # Drawing Venus
    pygame.draw.circle(screen, (193, 143, 23), venus_center, venus_radius)

    # Creating the path of Earth
    earth_angle += earth_animation_speed
    earth_x = center[0] + (sun_radius + 150) * math.cos(earth_angle * math.pi / 180)
    earth_y = center[1] + (sun_radius + 150) * math.sin(earth_angle * math.pi / 180)
    earth_center = (int(earth_x), int(earth_y))

    # Drawing Earth
    pygame.draw.circle(screen, (107, 147, 214), earth_center, earth_radius)

    # Creating the path of our Moon
    moon_angle += moon_animation_speed
    moon_x = earth_x + (earth_radius + 15) * math.cos(moon_angle * math.pi / 180)
    moon_y = earth_y + (earth_radius + 15) * math.sin(moon_angle * math.pi / 180)
    moon_center = (int(moon_x), int(moon_y))

    # Drawing our Moon
    pygame.draw.circle(screen, (246, 241, 213), moon_center, moon_radius)

    # Creating the path of Mars
    mars_angle += mars_animation_speed
    mars_x = center[0] + (sun_radius + 200) * math.cos(mars_angle * math.pi / 180)
    mars_y = center[1] + (sun_radius + 200) * math.sin(mars_angle * math.pi / 180)
    mars_center = (int(mars_x), int(mars_y))

    # Drawing Mars
    pygame.draw.circle(screen, (226, 123, 88), mars_center, mars_radius)

    # Creating the path of Jupiter
    jupiter_angle += jupiter_animation_speed
    jupiter_x = center[0] + (sun_radius + 300) * math.cos(jupiter_angle * math.pi / 180)
    jupiter_y = center[1] + (sun_radius + 300) * math.sin(jupiter_angle * math.pi / 180)
    jupiter_center = (int(jupiter_x), int(jupiter_y))

    # Drawing Jupiter
    pygame.draw.circle(screen, (201, 144, 57), jupiter_center, jupiter_radius)

    # Creating the path of Saturn
    saturn_angle += saturn_animation_speed
    saturn_x = center[0] + (sun_radius + 400) * math.cos(saturn_angle * math.pi / 180)
    saturn_y = center[1] + (sun_radius + 400) * math.sin(saturn_angle * math.pi / 180)
    saturn_center = (int(saturn_x), int(saturn_y))

    # Drawing Saturn
    pygame.draw.circle(screen, (191, 189, 175), saturn_center, saturn_radius)

    # Drawing Saturn's Rings
    pygame.draw.circle(screen, (184, 156, 114), saturn_center, rings_radius, 4)

    # Creating the path of Uranus
    uranus_angle += uranus_animation_speed
    uranus_x = center[0] + (sun_radius + 500) * math.cos(uranus_angle * math.pi / 180)
    uranus_y = center[1] + (sun_radius + 500) * math.sin(uranus_angle * math.pi / 180)
    uranus_center = (int(uranus_x), int(uranus_y))

    # Drawing Uranus
    pygame.draw.circle(screen, (178, 214, 219), uranus_center, uranus_radius)

    # Creating the path of Neptune
    neptune_angle += neptune_animation_speed
    neptune_x = center[0] + (sun_radius + 600) * math.cos(neptune_angle * math.pi / 180)
    neptune_y = center[1] + (sun_radius + 600) * math.sin(neptune_angle * math.pi / 180)
    neptune_center = (int(neptune_x), int(neptune_y))

    # Drawing Neptune
    pygame.draw.circle(screen, (41, 144, 181), neptune_center, neptune_radius)

    # Updating the screen
    pygame.display.flip()

pygame.quit()
