import os
import pygame
DIRNAME = os.path.dirname(__file__)

def load_image(file):
    return pygame.image.load(os.path.join(DIRNAME, "images", file))