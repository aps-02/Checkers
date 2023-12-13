# In This toss is being between the players and turn will be shown in terminal/output section 
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimaxwitha_b

FPS = 60

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main2():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers')
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)   
    while run:
        clock.tick(FPS)
        


        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()
    
def main1():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Checkers')
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)     
    alpha = float('-inf')
    beta = float('inf')
    while run:
        clock.tick(FPS)
         
        if game.turn == WHITE:
            value, new_board = minimaxwitha_b(game.get_board(),4, WHITE, game,alpha,beta)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()
        
n=int(input("Enter number of players:",))
while(n):
    if n==1:
       main1()
       n=0
    elif n==2:
       main2() 
       n=0  
    else:
        n=int(input("You have entered number of players more than 2 so please select number of playes less than 2 else type 0 to Quit:"),)