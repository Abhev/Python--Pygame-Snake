import time # importing modules
import random
import pygame

#Using Pygame
pygame.init() # INitalizing Pygame
# COlors variables with rgb combination is lcated below //

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
purple = (139,0,139)
red = (213, 50, 80)
green = (0, 255, 0)
pink = 	(255,20,147)
blue = (50, 153, 213)
colors = [purple,green,yellow,pink]
choosed_c = random.choice(colors)
dis_width = 600
dis_height = 400
#screen size
display = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake Game by Abhev J - Pygame")# screen name

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
#YOur score function
def Your_score(score) :
    value = score_font.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])
    # Our snake is being made below
def our_snake(snake_block, snake_list):
    
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])
    # it is displaying a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width / 6, dis_height / 3])
 
# main loop of the game

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0 # change in coordinates
 
    snake_List = []
    Length_of_snake = 1 # length of the snake
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True :
            display.fill(blue)
            message("You Lost! Press P to Play Again or 1 to Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c or event.key == pygame.K_p:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, choosed_c, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody :
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0)* 10.0
            
            Length_of_snake += 1
        clock.tick(snake_speed)
        

    pygame.quit()
    quit()
gameLoop()


