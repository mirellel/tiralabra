import pygame
from screen import Screen
from game import MainGame


def main():
    pygame.init()
    screen = Screen()
    game = MainGame()

    game.run()

if __name__ == "__main__":
    main()