import pygame
import datetime

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
X_OFFSET = 150
Y_OFFSET = 50

# Load the clock image and set the dimensions
clock_img = pygame.image.load('assets/img/Clock.png')
WIDTH, HEIGHT = clock_img.get_width(), clock_img.get_height()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image Clock")

# Mapping for the image filenames
filename_mapping = {
    0: "Zero.png",
    1: "One.png",
    2: "Two.png",
    3: "Three.png",
    4: "Four.png",
    5: "Five.png",
    6: "Six.png",
    7: "Seven.png",
    8: "Eight.png",
    9: "Nine.png"
}


# Load images using the filename mapping
number_images = {num: pygame.image.load(f'assets/img/{filename}') for num, filename in filename_mapping.items()}

def display_time():
    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw the clock image
    screen.blit(clock_img, (0, 0))

    now = datetime.datetime.now()
    hour, minute = now.hour, now.second

    # Get the individual digits of hour and minute
    hour_digits = [hour // 10, hour % 10]
    minute_digits = [minute // 10, minute % 10]

    # Draw the digits
    for i, digit in enumerate(hour_digits):
        screen.blit(number_images[digit], (20 + i * X_OFFSET, Y_OFFSET))

    # Draw the digits
    for i, digit in enumerate(minute_digits):
        screen.blit(number_images[digit], (330 + i * X_OFFSET, Y_OFFSET))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_time()
    pygame.display.flip()  # Update the whole screen
    clock.tick(1)  # Update once every second

pygame.quit()
