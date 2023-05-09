'''Moduuli, joka kuuluu UI:sta vastaaviin moduuleihin'''
import pygame

class MenuUI:
    '''Luokka, joka vastaa aloitusmenun UI:sta'''
    def __init__(self):
        self.screen = pygame.display.set_mode((700, 850))
        self.two_player_button = pygame.Rect(100, 300, 500, 150)
        self.singleplayer_button = pygame.Rect(100, 500, 500, 150)
        self.easy_button = pygame.Rect(50, 500, 150, 120)
        self.medium_button = pygame.Rect(270, 500, 170, 120)
        self.hard_button = pygame.Rect(500, 500, 150, 120)
        '''Tarvittavia värejä ja fontti'''
        self.red = (149, 18, 18)
        self.black = (0, 0, 0)
        self.light_grey = (143, 141, 141)
        self.dark_grey = (94, 90, 90)
        pygame.font.init()
        self.font = pygame.font.SysFont("EB Garamond", 40)

    def setup(self):
        '''Asettaa otsikon'''
        pygame.display.set_caption("NELJÄN SUORA - Twilight Edition")

    def draw_text(self, text, x_value, y_value):
        '''Funktio vastaa teksin kirjoittamisesta'''
        text_area = self.font.render(text, True, (self.black))
        self.screen.blit(text_area, (x_value, y_value))

    def draw_button(self, button, color):
        '''Funktio vastaa nappien piirtämisestä'''
        pygame.draw.rect(self.screen, color, button)

    def draw_screen_not_clicked(self):
        '''Funktio, joka piirtää ruudun hyödyntäen
        draw_text() ja draw_button() funktioita'''
        mouse = pygame.mouse.get_pos()
        buttons = [self.two_player_button, self.singleplayer_button]
        self.screen.fill(self.red)
        self.draw_text("OLETKO VALMIS PELAAMAAN?", 75, 80)

        for button in buttons:
            self.draw_button(button, self.dark_grey)
            if button.collidepoint(mouse):
                self.draw_button(button, self.light_grey)

        self.draw_text("VALITSE VASTUSTAJASI:", 120, 200)
        self.draw_text("KAVERI (2 PELAAJAA)", 150, 350)
        self.draw_text("TIETOKONE", 200, 550)
        pygame.display.flip()

    def draw_screen_clicked(self):
        '''Funktio, joka piirtää ruudun hyödyntäen
        draw_text() ja draw_button() funktioita'''
        mouse = pygame.mouse.get_pos()
        buttons = [self.two_player_button, self.easy_button,
                   self.medium_button, self.hard_button]
        self.screen.fill(self.red)
        self.draw_text("OLETKO VALMIS PELAAMAAN?", 75, 80)

        for button in buttons:
            self.draw_button(button, self.dark_grey)
            if button.collidepoint(mouse):
                self.draw_button(button, self.light_grey)

        self.draw_text("VALITSE VASTUSTAJASI:", 120, 200)
        self.draw_text("KAVERI (2 PELAAJAA)", 150, 350)
        self.draw_text("Jacob", 80, 520)
        self.draw_text("(helppo)", 60, 560)
        self.draw_text("Bella", 310, 520)
        self.draw_text("(keskitaso)", 275, 560)
        self.draw_text("Edward", 515, 520)
        self.draw_text("(vaikea)", 515, 560)
        pygame.display.flip()
