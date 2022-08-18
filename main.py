import pygame
from game import *
from game import checkForNeighbor as Neighbor
from game import update as upd
from constants import *
from pygame import mixer

# --- Initialization ---
pygame.init()
font = pygame.font.Font(None, 18)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Game()
mixer.music.load('gamemusic.mp3')
mixer.music.play(-1)
# --- Definition and starting screen---
color = pygame.Color('white')
text1 = font.render("Press Space bar, click the cells you want to make alive and press p to play", True, color)
text_rect = ""
background = pygame.surface.Surface(screen.get_size())
rect1 = pygame.draw.rect(background, pygame.Color('black'), [150, 150, 150, 150])
screen.blit(background, rect1)
screen.blit(text1, text1.get_rect(center=rect1.center))
running = True


def start():
    # --- Divide the board to parts of 60
    for x in range(0, SCREEN_WIDTH, 60):
        for y in range(0, SCREEN_HEIGHT, 60):
            rect = pygame.draw.rect(background, color, [x, y, 56, 56])  # --- Create rect ---
            screen.blit(background, rect)
            rectangels.append(rect)


# --- This function turns alive the cells the player chose----#
def click():
    # --- Iterate over the rect we have ----#
    for p in range(0, len(rectangels)):
        # get the x, y positions of the mouse click
        if rectangels[p].collidepoint(pygame.mouse.get_pos()):
            wake(p)
            # --- Update the game object
            print(p % game.size, p // game.size)
            game.matrix[p % game.size][p // game.size].state = True
            game.listOfAliveCells.append([int(p % game.size), int(p // game.size)])


# --- This function set the visuals of living cells ----
def wake(position):
    # --- Color the rect green and than change text ----
    screen.fill(pygame.Color("green"), rectangels[position])
    pygame.time.wait(100)
    pygame.display.update()
    return


def kill(position):
    # --- Color the rect gray and then change text ----
    pygame.time.wait(100)
    screen.fill(GRAY_1, rectangels[position])
    pygame.display.update()
    pygame.time.wait(100)
    screen.fill(pygame.Color('white'), rectangels[position])
    pygame.display.update()
    return


# --- This function Handle the game turns
def living():
    run = True
    while run:
        if len(game.listOfAliveCells) == 0:
            run = False
        game.matrix = Neighbor(game.matrix, game.listOfAliveCells)
        kill_for_update()
        game.matrix, game.listOfAliveCells = upd(game.matrix, game.listOfAliveCells)
        wake_for_update()
        for event1 in pygame.event.get():
            if event1.type == pygame.KEYUP:
                if event1.key == pygame.K_s or event1.type == pygame.QUIT:
                    pygame.quit()


def wake_for_update():
    for j in range(len(game.listOfAliveCells)):
        row = game.listOfAliveCells[j][0]
        column = game.listOfAliveCells[j][1]
        if game.matrix[row][column].state == True:
            wake(column * game.size + row)


def kill_for_update():
    for j in range(len(game.listOfAliveCells)):
        row = game.listOfAliveCells[j][0]
        column = game.listOfAliveCells[j][1]
        cell = game.matrix[row][column]
        if cell.counter <= 1 or cell.counter > 3:
            kill(column * game.size + row)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            # --- If space is pressed initialize board ---
            if event.key == pygame.K_SPACE:
                screen.fill(pygame.Color("black"))
                start()
            if event.key == pygame.K_p:
                living()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # --- Get user inputs ----
            click()

    pygame.display.flip()

# --- end ---#

pygame.quit()
