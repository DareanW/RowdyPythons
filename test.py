import pygame
import time
import random
#pip install pygame
pygame.init()
white = (255,255,255)
blue = (0,0,255)
black = (0, 0, 0)
red = (255,0,0)

dis_width = 400
dis_height = 300
dis = pygame.display.set_mode((dis_width, dis_width))

pygame.display.set_caption('Rowdy Pythons - Snake Game')

game_over=False

x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0



clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

def gameLoop():  # creating a function
    direction = ""
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            #print(event)   #prints out all the actions that take place on the screen
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != "right":
                    direction = "left"
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and direction != "left":
                    direction = "right"
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and direction != "down":
                    direction = "up"
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and direction != "up":
                    direction = "down"
                    y1_change = snake_block
                    x1_change = 0
                
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
 
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()