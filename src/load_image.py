'''Moduuli joka sisältää funktion load_image'''
import os
import pygame
DIRNAME = os.path.dirname(__file__)

def load_image(file):
    '''Funktio, joka lataa kuvat liikutettavista pelinappuloista'''
    return pygame.image.load(os.path.join(DIRNAME, "images", file))
