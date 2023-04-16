'''Moduuli, joka kuuluu UI:sta vastaaviin moduuleihin'''
import pygame

class MenuUI:
    '''Luokka, joka vastaa aloitusmenun UI:sta'''
    def __init__(self):
        self.screen = pygame.display.set_mode((700, 700))
        self.two_player_button = pygame.Rect(100, 200, 500, 150)
        self.singleplayer_button = pygame.Rect(100, 400, 500, 150)
        '''Tarvittavia värejä ja fontti'''
        self.red = (153, 37, 37)
        self.black = (0, 0, 0)
        self.light_grey = (143, 141, 141)
        self.dark_grey = (115, 114, 114)
        pygame.font.init()
        self.font = pygame.font.SysFont("EB Garamond", 40)

    def setup(self):
        '''Asettaa otsikon'''
        pygame.display.set_caption("Connect 4")

    def draw_text(self, text, x_value, y_value):
        '''Funktio vastaa teksin kirjoittamisesta'''
        text_area = self.font.render(text, True, (self.black))
        self.screen.blit(text_area, (x_value, y_value))

    def draw_button(self, button, color):
        '''Funktio vastaa nappien piirtämisestä'''
        pygame.draw.rect(self.screen, color, button)

    def draw_screen(self):
        '''Funktio, joka piirtää ruudun hyödyntäen
        draw_text() ja draw_button() funktioita'''
        mouse = pygame.mouse.get_pos()
        self.screen.fill(self.red)
        self.draw_text("VALITSE VASTUSTAJASI:", 120, 100)

        self.draw_button(self.two_player_button, self.dark_grey)
        if self.two_player_button.collidepoint(mouse):
            self.draw_button(self.two_player_button, self.light_grey)
        self.draw_text("KAVERI (2 PELAAJAA)", 150, 250)

        self.draw_button(self.singleplayer_button, self.dark_grey)
        if self.singleplayer_button.collidepoint(mouse):
            self.draw_button(self.singleplayer_button, self.light_grey)
        self.draw_text("TIETOKONE (HELPPO)", 150, 450)
        pygame.display.flip()
