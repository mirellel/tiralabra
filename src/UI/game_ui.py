'''Moduuli, joka kuuluu UI:sta vastaaviin moduuleihin'''
import pygame
from load_image import load_image

class GameUI:
    """Luokka, joka vastaa pelilaudan UI:sta"""

    def __init__(self):
        """Alustaa pelin attribuutit"""

        self.rows = 6
        self.cols = 7
        self.square_size = 100
        self.width = self.cols*self.square_size
        self.height = (self.rows+1)*self.square_size

        self.radius = self.square_size//2-5

        self.green = (53, 240, 103)
        self.red = (240, 53, 53)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.darkred = (153, 37, 37)

        pygame.font.init()
        self.font = pygame.font.SysFont("EB Garamond", 40)

    def setup(self):
        '''Funktio, joka määrittää pygame ikkunan ja sen otsikon'''
        self.screen = pygame.display.set_mode((self.width, self.height+150))
        pygame.display.set_caption("CONNECT 4")

    def draw_board(self, board, game_over, mouse_position, green_turn,
                   green_win, red_win, ai_player, tie, opponent):
        '''Funktio, joka piirtää pelilaudan, joka koostuu neiliöistä ja ympyröistä.'''
        self.screen.fill(self.white)
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(self.screen, self.black, (col*self.square_size,
                                                          row*self.square_size+self.square_size,
                                                          self.square_size, self.square_size))
                pygame.draw.circle(self.screen, self.white, (col*self.square_size+
                                                             self.square_size//2,
                                                             row*self.square_size+
                                                             self.square_size+
                                                             self.square_size//2), self.radius)
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] == 1:
                    pygame.draw.circle(self.screen, self.green, (col*self.square_size+
                                                                 self.square_size//2,
                                                                 self.height-
                                                                 (row*self.square_size+
                                                                  self.square_size//2)),
                                                                 self.radius)

                elif board[row][col] == 2:
                    pygame.draw.circle(self.screen, self.red, (col*self.square_size+
                                                               self.square_size//2,
                                                                 self.height-
                                                                 (row*self.square_size+
                                                                  self.square_size//2)),
                                                                 self.radius)
        if opponent != "player":
            self.draw_opponent(opponent)
        if game_over:
            if tie:
                self.draw_tie()
            else:
                self.draw_victory(green_win, red_win)
        if not game_over:
            self.draw_piece(mouse_position, green_turn, ai_player)
            pygame.display.flip()
        pygame.display.update()
        pygame.display.flip()

    def draw_piece(self, mouse_position, green_turn, ai_player):
        '''Funktio, joka piirtää liikutettavan pelinappulan pelilaudan
        yläpuolelle'''
        x_cordinate = mouse_position[0]
        x_cordinate -=50
        green_piece = load_image("green.png")
        red_piece = load_image("red.png")
        if x_cordinate < 0:
            x_cordinate = 0
        if x_cordinate > 600:
            x_cordinate = 600
        if green_turn:
            self.screen.blit(green_piece, (x_cordinate, 0))

        else:
            if ai_player:
                ai_text = self.font.render("lasketaan siirtoa", True, (0, 0, 0))
                self.screen.blit(ai_text, (135, 25))
            else:
                self.screen.blit(red_piece, (x_cordinate, 0))

    def draw_victory(self, green_win, red_win):
        '''Funktio, joka ilmoittaa voitosta'''
        if green_win:
            text = self.font.render("Vihreä pelaaja voitti!",
                                    True, (self.black))
        if red_win:
            text = self.font.render("Punainen pelaaja voitti!",
                                    True, (self.black))
        restart_text = self.font.render("Paina r palataksesi Menuun", True,
                                        self.black)
        self.screen.blit(text, (120, 10))
        self.screen.blit(restart_text, (100, 45))

    def draw_tie(self):
        '''Funktio, joka ilmoittaa voitosta'''
        text = self.font.render("Tasapeli!",
                                    True, (self.black))
        restart_text = self.font.render("Paina r palataksesi Menuun", True,
                                        self.black)
        self.screen.blit(text, (120, 10))
        self.screen.blit(restart_text, (100, 45))

    def draw_opponent(self, opponent):
        self.opponent = load_image(f"twilight_{opponent}.png")
        self.screen.blit(self.opponent, (0, 700))
