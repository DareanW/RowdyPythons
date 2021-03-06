import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (73, 17, 107)
 
dis_width = 600
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Python Game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_block2 = 10
snake_speed = 15
snake_speed2 = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)
 
 
def Your_score1(score):
    value = score_font.render("Player 1 Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def Your_score2(score2):
    value = score_font.render("Player 2 Score: " + str(score2), True, yellow)
    dis.blit(value, [300, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def our_snake2(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    direction = ""
    direction2 = ""
    winner = ""
    speed = 0
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
    x2 = dis_width / 2
    y2 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
    x2_change = 0
    y2_change = 0
 
    snake_List = []
    snake_List2 = []
    Length_of_snake = 1
    Length_of_snake2 = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    shortx = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    shorty = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    speedupx = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    speedupy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    speeddownx = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    speeddowny = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score1(Length_of_snake - 1)
            Your_score2(Length_of_snake2 - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and direction2 != "right":
                    direction2 = "left"
                    x2_change = -snake_block
                    y2_change = 0
                elif event.key == pygame.K_d and direction2 != "left":
                    direction2 = "right"
                    x2_change = snake_block
                    y2_change = 0
                elif event.key == pygame.K_w and direction2 != "down":
                    direction2 = "up"
                    y2_change = -snake_block
                    x2_change = 0
                elif event.key == pygame.K_s and direction2 != "up":
                    direction2 = "down"
                    y2_change = snake_block
                    x2_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
            winner = "Snake 2"
        if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
            game_close = True
            winner = "Snake 1"

        if Length_of_snake - 1 == -1:
            game_close = True    

        if Length_of_snake2 - 1 == -1:
            game_close = True    

        x1 += x1_change
        x2 += x2_change
        y1 += y1_change
        y2 += y2_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, yellow, [speedupx, speedupy, snake_block, snake_block])
        pygame.draw.rect(dis, purple, [speeddownx, speeddowny, snake_block, snake_block])
        pygame.draw.rect(dis, red, [shortx, shorty, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        snake_Head2 = []
        snake_Head2.append(x2)
        snake_Head2.append(y2)
        snake_List2.append(snake_Head2)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        if len(snake_List2) > Length_of_snake2:
            del snake_List2[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for x in snake_List2[:-1]:
            if x == snake_Head2:
                game_close = True
 
    
        our_snake2(snake_block2, snake_List2)
        Your_score2(Length_of_snake2 - 1)

        our_snake(snake_block, snake_List)
        Your_score1(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        if x2 == foodx and y2 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block2) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block2) / 10.0) * 10.0
            Length_of_snake2 += 1


 
        if x1 == shortx and y1 == shorty:
            shortx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            shorty = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1

            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.remove(snake_Head)

        if x2 == shortx and y2 == shorty:
            shortx = round(random.randrange(0, dis_width - snake_block2) / 10.0) * 10.0
            shorty = round(random.randrange(0, dis_height - snake_block2) / 10.0) * 10.0
            Length_of_snake2 -= 1

            snake_Head2.append(x2)
            snake_Head2.append(y2)
            snake_List2.remove(snake_Head2)    



        if x1 == speedupx and y1 == speedupy:
            speedupx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            speedupy = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            if(snake_speed + speed >= 39): # Speed up Limit.
                clock.tick(snake_speed + speed)

            else:
                speed += 3 
                clock.tick(snake_speed + speed)

        else:
            clock.tick(snake_speed + speed)

        if x2 == speedupx and y2 == speedupy:
            speedupx = round(random.randrange(0, dis_width - snake_block2) / 10.0) * 10.0
            speedupy = round(random.randrange(0, dis_height - snake_block2) / 10.0) * 10.0
            if(snake_speed2 + speed >= 39): # Speed up Limit.
                clock.tick(snake_speed2 + speed)

            else:
                speed += 3 
                clock.tick(snake_speed2 + speed)

        else:
            clock.tick(snake_speed2 + speed)    



        if x1 == speeddownx and y1 == speeddowny:
            speeddownx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            speeddowny = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            if(speed + snake_speed <= 15): # Speed down Limit.
                clock.tick(snake_speed + speed)

        


            else:
                speed = speed - 3
                clock.tick(snake_speed + speed)

        else:
            clock.tick(snake_speed + speed)

        if x2 == speeddownx and y2 == speeddowny:
            speeddownx = round(random.randrange(0, dis_width - snake_block2) / 10.0) * 10.0
            speeddowny = round(random.randrange(0, dis_height - snake_block2) / 10.0) * 10.0
            if(speed + snake_speed2 <= 15): # Speed down Limit.
                clock.tick(snake_speed2 + speed)

        


            else:
                speed = speed - 3
                clock.tick(snake_speed2 + speed)

        else:
            clock.tick(snake_speed2 + speed)

    pygame.quit()
    quit()
 
 
gameLoop()
