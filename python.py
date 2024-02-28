import pygame
import time
import random

pygame.init()

screen_width = 800
screen_height = 600
block_size = 20
fps = 15

white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

font_style = pygame.font.SysFont(None, 50)

game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Zoqanch game')

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 15

def score(score):
    value = font_style.render("Miavor: " + str(score), True, black)
    game_display.blit(value, [0, 0])

def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [screen_width / 6, screen_height / 3])

def game_loop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    foody = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    while not game_over:

        while game_close:
            game_display.fill(white)
            message("Krvar  C- eli xaxal  Q-sxme rad exnel ", red)
            score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(blue)

        pygame.draw.rect(game_display, red, [foodx, foody, block_size, block_size])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(block_size, snake_list)
        score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            foody = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
