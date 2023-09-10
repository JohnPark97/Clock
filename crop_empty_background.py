import os
import pygame

def get_bounding_box(surface):
    min_x = surface.get_width() - 1
    max_x = 0
    min_y = surface.get_height() - 1
    max_y = 0

    for y in range(surface.get_height()):
        for x in range(surface.get_width()):
            if surface.get_at((x, y))[3] > 0:
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)

    return  (23, 13, 103, 217)
    # return (min_x, min_y, max_x - min_x + 1, max_y - min_y + 1)

def crop_transparent(surface):
    bbox = get_bounding_box(surface)
    cropped_surf = pygame.Surface((bbox[2], bbox[3]), pygame.SRCALPHA)
    cropped_surf.blit(surface, (0, 0), area=bbox)
    return cropped_surf

pygame.init()

# Path to the directory
directory = 'assets/img'

# Iterate over all files in the directory
# for filename in os.listdir(directory):
    # Check if the file is a .png image
    # if filename.endswith('.png'):
filename = 'One.png'
filepath = os.path.join(directory, filename)

# Load the image using pygame
image = pygame.image.load(filepath)

# Crop the image to its non-transparent area
cropped_image = crop_transparent(image)

# Save the cropped image with the prefix 'cropped_'
cropped_filepath = os.path.join(directory, 'cropped_' + filename)
pygame.image.save(cropped_image, cropped_filepath)



pygame.quit()
