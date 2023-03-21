import pygame

class Screen:
    """Luokka, joka huolehtii Pygame näytöstä peliä varten"""

    def __init__(self):
        pygame.init()
        self._width = 700
        self._height = 900

        self._screen = pygame.display.set_mode((self._width, self._height))
