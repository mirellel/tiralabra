'''Moduuli, joka kuuluu UI:sta vastaaviin moduuleihin'''
import pygame
from load_image import load_image

class GameUI:
    """Luokka, joka vastaa pelilaudan UI:sta"""

    def __init__(self):
        """Alustaa pelin attribuutit"""

        '''Pelilaudan rivien ja sarakkeiden määrät, pelilaudan koko'''
        self.rows = 6
        self.cols = 7
        self.square_size = 100
        self.width = self.cols*self.square_size
        self.height = (self.rows+1)*self.square_size

        self.radius = self.square_size//2-5
        
        self.green = (53, 240, 103)
        self.red = (240, 53, 53)
        self.blue = (111, 163, 189)
        self.white = (255, 255, 255)

        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 40, 1)
    
    def setup(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("CONNECT 4")
    
    def draw_board(self, board, game_over, mouse_position, green_turn, green_win, red_win):
        '''Funktio, joka piirtää pelilaudan, joka koostuu neiliöistä ja ympyröistä.'''
        self.screen.fill(self.white)
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(self.screen, self.blue, (col*self.square_size, row*self.square_size+self.square_size, self.square_size, self.square_size))
                pygame.draw.circle(self.screen, self.white, (col*self.square_size+self.square_size//2, row*self.square_size+self.square_size+self.square_size//2), self.radius)
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] == 1:
                    pygame.draw.circle(self.screen, self.green, (col*self.square_size+self.square_size//2, 
                                                                 self.height- 
                                                                 (row*self.square_size+self.square_size//2)), 
                                                                 self.radius)
                elif board[row][col] == 2:
                    pygame.draw.circle(self.screen, self.red, (col*self.square_size+self.square_size//2, 
                                                                 self.height- 
                                                                 (row*self.square_size+self.square_size//2)), 
                                                                 self.radius)
        if game_over:
            self.draw_victory(green_win, red_win)
        if not game_over:
            self.draw_piece(mouse_position, green_turn)
            pygame.display.flip()
        pygame.display.update()
        pygame.display.flip()

    

    def draw_piece(self, mouse_position, green_turn):
        x = mouse_position[0]
        x -=50
        green_piece = load_image("green.png")
        red_piece = load_image("red.png")
        if x < 0:
            x = 0
        if x > 600:
            x = 600
        if green_turn:
            self.screen.blit(green_piece, (x, 0))
        
        else:
            self.screen.blit(red_piece, (x, 0))

    def draw_victory(self, green_win, red_win):
        if green_win == True:
            text = self.font.render("Vihreä pelaaja voitti!",
                                    True, (self.green))
        if red_win == True:
            text = self.font.render("Punainen pelaaja voitti!",
                                    True, (self.red))
        restart_text = self.font.render("Paina r palataksesi Menuun", True, 
                                        self.blue)
        pygame.time.wait(1000)
        self.screen.fill(self.white)
        self.screen.blit(text, (120, self.height/2))
        self.screen.blit(restart_text, (100, 400))