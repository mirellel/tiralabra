import pygame
from files.game import MainGame
from UI.menu_ui import MenuUI

class Menu:
    '''Funktio, joka vastaa aloitusmenun logiikasta'''
    def __init__(self):
        self.ui = MenuUI()

    def run_menu(self):
        '''Pyörittää menua'''
        pygame.init()
        self.ui.setup()
        self.menu_loop()


    def handle_events(self):
        '''Funktio, joka käsittelee pygame tapahtumia'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = pygame.mouse.get_pos()
                    self.mouse_click(position)

    def draw_screen(self):
        '''Funktio kutsuu UI:n samannimistä funktiota piirtämään ruudun'''
        self.ui.draw_screen()

    def menu_loop(self):
        '''Kutsuu funktioita, jotka piirtävät ruudut ja
        käsittelevät tapahtumat pelin sammumiseen asti'''
        while True:
            self.handle_events()
            self.draw_screen()

    def mouse_click(self, position):
        '''Käsittelee hiirenklikkejä'''
        if self.ui.two_player_button.collidepoint(position):
            two_player_game = MainGame()
            two_player_game.run()
