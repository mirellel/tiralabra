'''Moduuli, joka kuuluu UI:sta vastaaviin moduuleihin'''
import pygame

class MenuUI:
    '''Luokka, joka vastaa aloitusmenun UI:sta'''
    def __init__(self):
        self.screen = pygame.display.set_mode((700, 700))
        self.two_player_button = pygame.Rect(100, 200, 500, 150)
        self.singleplayer_button = pygame.Rect(100, 400, 500, 150)
        '''Tarvittavia värejä ja fontti'''
        self.white = (255, 255, 255)
        self.green = (180, 224, 166)
        self.blue = (111, 163, 189)
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 40, 1)

    def setup(self):
        '''Asettaa otsikon'''
        pygame.display.set_caption("Connect 4")

    def draw_text(self, text, x_value, y_value):
        '''Funktio vastaa teksin kirjoittamisesta'''
        text_area = self.font.render(text, True, (self.blue))
        self.screen.blit(text_area, (x_value, y_value))

    def draw_button(self, button):
        '''Funktio vastaa nappien piirtämisestä'''
        pygame.draw.rect(self.screen, self.green, button)

    def draw_screen(self):
        '''Funktio, joka piirtää ruudun hyödyntäen
        draw_text() ja draw_button() funktioita'''
        self.screen.fill(self.white)
        self.draw_text("Valitse vastustajasi:", 120, 100)
        self.draw_button(self.two_player_button)
        self.draw_text("Kaveri (2 pelaajaa)", 150, 250)
        self.draw_button(self.singleplayer_button)
        self.draw_text("Tietokone (tulossa)", 150, 450)
        pygame.display.flip()
