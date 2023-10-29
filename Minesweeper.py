import pygame
import random

pygame.init()



background = pygame.image.load('images\\background.bmp')
background_rect = background.get_rect()

Minesweeper = pygame.image.load('images\\true\\Minesweeper.bmp')
Minesweeper_rect = Minesweeper.get_rect()

one = pygame.image.load('images\\true\\1.bmp')
one_rect = one.get_rect()

two = pygame.image.load('images\\true\\2.bmp')
two_rect = two.get_rect()

three = pygame.image.load('images\\true\\3.bmp')
three_rect = three.get_rect()

four = pygame.image.load('images\\true\\4.bmp')
four_rect = four.get_rect()

five = pygame.image.load('images\\true\\5.bmp')
five_rect = five.get_rect()

six = pygame.image.load('images\\true\\6.bmp')
six_rect = six.get_rect()

seven = pygame.image.load('images\\true\\7.bmp')
seven_rect = seven.get_rect()

eight = pygame.image.load('images\\true\\8.bmp')
eight_rect = eight.get_rect()


die = pygame.image.load('images\\Others\\die.bmp')
die_rect = die.get_rect()

opes = pygame.image.load('images\\Others\\opes.bmp')
opes_rect = opes.get_rect()

smile = pygame.image.load('images\\Others\\smile.bmp')
smile_rect = smile.get_rect()


flag = pygame.image.load('images\\Others\\flag.bmp')
flag_rect = flag.get_rect()

what = pygame.image.load('images\\Others\\what.bmp')
what_rect = what.get_rect()


alllist = [

    {
        0:[0,False],
        1:[0,False],
        2:[0,False],
        3:[0,False],
        4:[0,False],
        5:[0,False],
        6:[0,False],
        7:[0,False],
        8:[0,False],
        9:[0,False]
    },    
    {
        0:[0,False],
        1:[0,False],
        2:[0,False],
        3:[0,False],
        4:[0,False],
        5:[0,False],
        6:[0,False],
        7:[0,False],
        8:[0,False],
        9:[0,False]
    },
        {
        0:[0,False],
        1:[0,False],
        2:[0,False],
        3:[0,False],
        4:[0,False],
        5:[0,False],
        6:[0,False],
        7:[0,False],
        8:[0,False],
        9:[0,False]
    },
        {
        0:[0,False],
        1:[0,False],
        2:[0,False],
        3:[0,False],
        4:[0,False],
        5:[0,False],
        6:[0,False],
        7:[0,False],
        8:[0,False],
        9:[0,False]
    },
        {
        0:[0,False],
        1:[0,False],
        2:[0,False],
        3:[0,False],
        4:[0,False],
        5:[0,False],
        6:[0,False],
        7:[0,False],
        8:[0,False],
        9:[0,False]
    },
        {
        0:[0,False],
        1:[0,False],
        2:[0,False],
        3:[0,False],
        4:[0,False],
        5:[0,False],
        6:[0,False],
        7:[0,False],
        8:[0,False],
        9:[0,False]
    },
        {
        0:[0,False],
        1:[0,False],
        2:[0,False],
        3:[0,False],
        4:[0,False],
        5:[0,False],
        6:[0,False],
        7:[0,False],
        8:[0,False],
        9:[0,False]
    },
        {
        0:[0,False],
        1:[0,False],
        2:[0,False],
        3:[0,False],
        4:[0,False],
        5:[0,False],
        6:[0,False],
        7:[0,False],
        8:[0,False],
        9:[0,False]
    },
        {
        0:[0,False],
        1:[0,False],
        2:[0,False],
        3:[0,False],
        4:[0,False],
        5:[0,False],
        6:[0,False],
        7:[0,False],
        8:[0,False],
        9:[0,False]
    },
        {
        0:[0,False],
        1:[0,False],
        2:[0,False],
        3:[0,False],
        4:[0,False],
        5:[0,False],
        6:[0,False],
        7:[0,False],
        8:[0,False],
        9:[0,False]
    },
]

for i in range(15):
    while True:
        x = random.randint(0,9)
        y = random.randint(0,9)
        if alllist[x][y][0] != 9:
            alllist[x][y][0] = 9
            try:
                if alllist[x-1][y-1][0] != 9:
                    alllist[x-1][y-1][0] += 1
            except:
                pass
            try:
                if alllist[x-1][y][0] != 9:
                    alllist[x-1][y][0] += 1
            except:
                pass
            try:
                if alllist[x-1][y+1][0] != 9:
                    alllist[x-1][y+1][0] += 1
            except:
                pass
            try:
                if alllist[x][y-1][0] != 9:
                    alllist[x][y-1][0] += 1
            except:
                pass
            try:
                if alllist[x][y+1][0] != 9:
                    alllist[x][y+1][0] += 1
            except:
                pass
            try:
                if alllist[x+1][y-1][0] != 9:
                    alllist[x+1][y-1][0] += 1
            except:
                pass
            try:
                if alllist[x+1][y][0] != 9:
                    alllist[x+1][y][0] += 1
            except:
                pass
            try:
                if alllist[x+1][y+1][0] != 9:
                    alllist[x+1][y+1][0] += 1
            except:
                pass
            
            break


screen = pygame.display.set_mode((378, 418))
color = (195, 195, 195)
state = smile
state_rect = smile_rect
state_rect = state_rect.move([170,1])
#主循环
whit = 0
background_rect = background_rect.move([0,40])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            whit = 1
    
    
    screen.fill(color)
    screen.blit(background, background_rect)
    screen.blit(state, state_rect)
    pygame.display.flip()
    if whit == 1:
        pygame.quit()
        break