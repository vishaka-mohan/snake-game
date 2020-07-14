import pygame
import math
import random

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("snake game")
green = (0, 255, 0)
blue = (0, 0, 255)
change_x = 0
change_y = 0
vel = 10
curr_x = 300
curr_y = 300
visible = True
clock = pygame.time.Clock()
high_score = 0


class snake(object):

    def __init__(self, color, x, y, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height


def my_score():
    pygame.font.init()
    font2 = pygame.font.SysFont('Comic Sans MS', 20)
    text1 = font2.render("YOUR SCORE: "+str(length-1), False, (255, 255, 255))
    win.blit(text1, (12,12))

    text2= font2.render("HIGH SCORE: "+str(high_score), False, (255,255,255))
    win.blit(text2, (400,12))
    pygame.display.update()


class food(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = blue

    def place_food(self):
        pygame.draw.circle(win, (0,0,255), (self.x,self.y), 7)
        pygame.display.update()


def redraw():
    global Mysnake
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (0, 0, 10, 600))
    pygame.draw.rect(win, (255, 0, 0), (0, 590, 600, 10))
    pygame.draw.rect(win, (255, 0, 0), (590, 0, 10, 600))
    pygame.draw.rect(win, (255, 0, 0), (0, 0, 600, 10))
    my_score()

    if visible == True:

        for mysnake in Mysnake:
            # print(len(Mysnake))
            pygame.draw.rect(win, mysnake.color, (mysnake.x, mysnake.y, 10, 10))

        snakefood.place_food()

    pygame.display.update()


def playagain():
    font1 = pygame.font.SysFont('Comic Sans MS', 20)
    text = font1.render("You Lost! Press P to play again", False, (255, 255, 0))

    win.blit(text, (150, 400))

    pygame.display.update()


Mysnake = []
length = 1
foodx = random.randint(20, 580)
foody = random.randint(50, 580)
snakefood = food(foodx, foody)
f = 0
playgame= True
lostgame = False


def play():
    global playgame, lostgame, curr_y, curr_x, visible, snakefood, change_y, change_x, length, Mysnake, f, high_score
    while playgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        while lostgame:
            redraw()
            playagain()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    playgame = False
                    lostgame = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        playgame = True
                        lostgame = False
                        visible = True
                        curr_x = 300
                        curr_y = 300
                        if length-1 >= high_score:
                            high_score = length-1
                        length = 1
                        Mysnake = []
                        play()


        clock.tick(vel)



        keys = pygame.key.get_pressed()

        if curr_x <= 5 or curr_x + 10 >= 595:
            visible = False

        if curr_y <= 5 or curr_y + 10 >= 595:
            visible = False

        if visible == True:

            snakefood.place_food()

            if keys[pygame.K_UP]:
                change_x = 0
                change_y = -vel

            elif keys[pygame.K_DOWN]:
                change_x = 0
                change_y = vel

            elif keys[pygame.K_LEFT]:
                change_x = -vel
                change_y = 0

            elif keys[pygame.K_RIGHT]:
                change_x = vel
                change_y = 0

            curr_y += change_y
            curr_x += change_x
            curr_snake = snake(green, curr_x, curr_y, 10, 10)


            Mysnake.append(curr_snake)
            if len(Mysnake) > length:
                del Mysnake[0]

            if curr_x >= snakefood.x-7 and curr_x <= snakefood.x+7:
                if curr_y >= snakefood.y -7 and curr_y <= snakefood.y+7:

                    length += 1
                    foodx = random.randint(10, 580)
                    foody = random.randint(20, 580)
                    snakefood = food(foodx, foody)

            for mysnake in Mysnake[:-1]:
                if mysnake.x == curr_snake.x and mysnake.y == curr_snake.y:
                    f = 1
                    visible = False

            redraw()

            pygame.display.update()




        else:


            #pygame.font.init()
            #font1 = pygame.font.SysFont('Comic Sans MS', 30)
            #text = font1.render("GAME OVER", False, (255, 0, 0))
            #win.blit(text, (300 - (text.get_width() / 2), 200))

            lostgame = True
            #if f == 1:

                #pygame.font.init()
                #font2 = pygame.font.SysFont('Comic Sans MS', 30)
                #text1 = font2.render("YOU BIT YOURSELF ", False, (255, 0, 0))
                #win.blit(text1, (100, 100))
                #pygame.display.update()

            #pygame.display.update()


play()
