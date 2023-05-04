'''Moduuli, joka sisältää Menusta huolehtivan luokan Menu'''
import pygame
from files.singleplayer import SinglePlayer
from files.multiplayer import MultiPlayer
from UI.menu_ui import MenuUI

easy = 2
medium = 4
hard = 6

class Menu:
    '''Funktio, joka vastaa aloitusmenun logiikasta'''
    def __init__(self):
        self.menu_ui = MenuUI()
        self.clicked = False

    def run_menu(self):
        '''Pyörittää menua'''
        pygame.init()
        self.menu_ui.setup()
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
        if self.clicked:
            self.menu_ui.draw_screen_clicked()
        else:
            self.menu_ui.draw_screen_not_clicked()

    def menu_loop(self):
        '''Kutsuu funktioita, jotka piirtävät ruudut ja
        käsittelevät tapahtumat pelin sammumiseen asti'''
        while True:
            self.handle_events()
            self.draw_screen()

    def mouse_click(self, position):
        '''Käsittelee hiirenklikkejä'''
        if self.menu_ui.two_player_button.collidepoint(position):
            two_player_game = MultiPlayer()
            two_player_game.run()
        if not self.clicked:
            if self.menu_ui.singleplayer_button.collidepoint(position):
                self.clicked = True
        else:
            if self.menu_ui.easy_button.collidepoint(position):
                singleplayer_game = SinglePlayer(easy)
                singleplayer_game.run()
            if self.menu_ui.medium_button.collidepoint(position):
                singleplayer_game = SinglePlayer(medium)
                singleplayer_game.run()
            if self.menu_ui.hard_button.collidepoint(position):
                singleplayer_game = SinglePlayer(hard)
                singleplayer_game.run()
