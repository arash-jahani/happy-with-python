import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('8 Queens Puzzle')

BOARD_SIZE = 8
SQUARE_SIZE = 75

board = [[0 for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

def is_valid_position(row,col):
    for i in range(row):
          if board[i][col] == 1:
               return False
          if col-i-1 >= 0 and board[row-i-1][col-i-1] == 1:
               return False
          if col+i+1 <BOARD_SIZE and board[row-i-1][col+i+1]==1:
               return False  
    return True

def solve_queens_puzzle(row):    
    if row >=BOARD_SIZE:
          return True
    for col in range(BOARD_SIZE):
          if is_valid_position(row,col):
               board[row][col] =1
               if solve_queens_puzzle(row+1):
                    return True
               board[row][col] =0
    return False

def draw_board():
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if(row+col) % 2 ==0:
                     color = WHITE
                else:
                     color = BLACK
                pygame.draw.rect(screen,color,(col * SQUARE_SIZE,row*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))


def draw_queens():
    for row in range(BOARD_SIZE):
         for col in range(BOARD_SIZE):
              if board[row][col]==1:
                   queen_image = pygame.image.load('queen.png')
                   queen_image = pygame.transform.scale(queen_image,(SQUARE_SIZE,SQUARE_SIZE))
                   screen.blit(queen_image,(col*SQUARE_SIZE,row*SQUARE_SIZE))

solve_queens_puzzle(0)

draw_board()
draw_queens()

pygame.display.update()


running = True
while running:
     for event in pygame.event.get():
          if(event.type==pygame.QUIT):
               running=False


pygame.quit()
        


        
