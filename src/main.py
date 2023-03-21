import pygame
from game import MainGame


def main():
    pygame.init()
    game = MainGame()

    game.run()

if __name__ == "__main__":
    main()