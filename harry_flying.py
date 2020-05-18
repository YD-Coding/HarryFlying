import pygame, sys
import math
import random
from pygame import mixer
from classes import Button
menu_run = True
BoostCounter = 100
DracoVel = 6
BludgerX_change = 15
SnitchSpeed = 100
running = None
HasBoost = False
main_win = None
ins_run = False
clock = pygame.time.Clock()
pygame.init()
pygame.font.init()

menu_background = pygame.image.load("menu.background.png")
instructions_image = pygame.image.load("instructions.png")

def instructions_win():
    global ins_run
    ins_run = True

    instructions_win = pygame.display.set_mode((650,500))

    while ins_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ins_run = False
                menu()

        instructions_win.blit(instructions_image,(0 ,0))
        pygame.display.update()

def create_main_win():
    global main_win
    main_win = pygame.display.set_mode((1200, 750))




play_button = Button((255, 255, 255), 170, 150, 300, 75, 'PLAY!', 72) 
easy_diff = Button((98, 253, 135), 15, 100, 300, 125, 'EASY', 60)
normal_diff = Button((0, 179, 255), 335, 100, 300, 125, 'NORMAL', 60)
hard_diff = Button((255, 222, 0), 15, 250, 300, 125, 'HARD', 60)
master_diff = Button((225, 0, 77), 335, 250, 300, 125, 'MASTER', 60)
ins_button = Button((255,255,255), 170, 230, 300, 75, 'INSTRUCTIONS', 45)

def menu():
    
    global running
    global DracoVel
    global SnitchSpeed
    global BludgerX_change
    
    menu_win = pygame.display.set_mode((650, 500))
    menu_cap = pygame.display.set_caption("MAIN MENU")            
    menu_run = True
    def redrawMenu():
        play_button.draw(menu_win, (0, 0, 0))
        ins_button.draw(menu_win, (0, 0, 0))
        
    while menu_run:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  
            if event.type == pygame.QUIT:
                menu_run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.isOver(pos):
                    def redrawMenu():
                        easy_diff.draw(menu_win, (0, 0, 0))
                        normal_diff.draw(menu_win, (0, 0, 0))
                        hard_diff.draw(menu_win, (0, 0, 0))
                        master_diff.draw(menu_win, (0, 0, 0))
                    redrawMenu()
                elif easy_diff.isOver(pos):
                    menu_run = False
                    DracoVel = 4
                    SnitchSpeed = 115
                    BludgerX_change = 10
                    running = True
                    create_main_win()
                    pygame.display.update()
                elif normal_diff.isOver(pos):
                    menu_run = False
                    DracoVel = 7
                    BludgerX_change = 15
                    SnitchSpeed = 90
                    running = True
                    create_main_win()
                    pygame.display.update()
                elif hard_diff.isOver(pos):
                    menu_run = False
                    DracoVel = 10
                    BludgerX_change = 30
                    SnitchSpeed = 50 
                    running = True
                    create_main_win()
                    pygame.display.update()
                elif master_diff.isOver(pos):
                    menu_run = False
                    DracoVel = 20
                    BludgerX_change = 40
                    SnitchSpeed = 25
                    running = True
                    create_main_win()
                    pygame.display.update()
                elif ins_button.isOver(pos):
                    menu_run = False
                    instructions_win()
                
            if event.type == pygame.MOUSEMOTION:
                if play_button.isOver(pos):
                    play_button.color = (211,211,211)
                elif easy_diff.isOver(pos):
                    easy_diff.color = (255, 255, 255)
                elif normal_diff.isOver(pos):
                    normal_diff.color = (255, 255, 255)
                elif hard_diff.isOver(pos):
                    hard_diff.color = (255, 255, 255)
                elif master_diff.isOver(pos):
                    master_diff.color = (255, 0, 0)
                elif ins_button.isOver(pos):
                    ins_button.color = (211, 211, 211)
                else:
                    play_button.color = (255, 255, 255)
                    easy_diff.color = (98, 253, 135)
                    normal_diff.color = (0, 179, 255)
                    hard_diff.color = (255, 222, 0)
                    master_diff.color = (225, 0, 77)
                    ins_button.color = (255, 255, 255)
                    #warning = pygame.font.SysFont('arial', 50)
                    #warning_text = warning.render("", True, (0, 0, 0))
                
        # create_main_win()       
        menu_win.blit(menu_background, (0,0))
        redrawMenu()
        pygame.display.update()
 


menu()              














    # DracoVel = 4
    # SnitchSpeed = 115
    # BludgerX_change = 10
    # running = True

    # DracoVel = 6
    # BludgerX_change = 15
    # SnitchSpeed = 100
    # running = True

    # DracoVel = 8
    # BludgerX_change = 20
    # SnitchSpeed = 75
    # running = True

    # DracoVel = 165
    # BludgerX_change = 35
    # SnitchSpeed = 45
    # running = True

    # DracoVel = 30
    # BludgerX_change = 45
    # SnitchSpeed = 30
    # running = True



GameState = True
isDown = False

# window, caption, background

main_cap = pygame.display.set_caption("QUIDDITCH")
background = pygame.image.load("Quidditchpitch.png")

# Harry
HarryImage = pygame.image.load("harry-potter-quidditch-world-cup-broom-harry-potter-and-the-order-of-the-phoenix-harry-potter-png-clip-art.png")
HarryX = 100
HarryY = 150
HarryVel = 12
BoostCounter = 0
def HarryFly():
    main_win.blit(HarryImage, (HarryX, HarryY))

#  Draco
DracoImage = pygame.image.load("draco.first!.png")
DracoX = 800
DracoY = 0



def DracoFly():
    main_win.blit(DracoImage, (DracoX, DracoY))
# Bludger
BludgerImage = pygame.image.load("bludger.png")
BludgerX = 700
BludgerY_change = 0
Bludger_state = "ready"

def shotbludger(x, y):
    global Bludger_state
    Bludger_state = "fire"
    main_win.blit(BludgerImage, (x - 10, y))

# Snitch
SnitchImage = pygame.image.load("Golden_Snitch..png")
SnitchX = random. randint(0, 500)
SnitchY = random.randint(0, 500)
SnitchCounter = 0

#snitch sound
SnitchSound = mixer.Sound("Gold (Sound Effect) Diablo II (mp3cut.net).wav")

def moveSnitch():
    global SnitchX
    global SnitchY
    global SnitchCounter
    global SnitchSpeed
    #!main_win.blit(SnitchImage, (SnitchX, SnitchY))
    if SnitchCounter > SnitchSpeed:
        SnitchX = random.randint(0, 500)
        SnitchY = random.randint(0, 500)
        SnitchCounter = 0
    else:
        SnitchCounter += 1
    main_win.blit(SnitchImage, (SnitchX, SnitchY))

Score = 0
ScoreText = pygame.font.Font('freesansbold.ttf', 40)
ScoreTextX = 975
ScoreTextY = 350


def showScore():
    ScoreTextR = ScoreText.render("Score : " + str(Score), True, (0, 0, 0))
    main_win.blit(ScoreTextR, (ScoreTextX, ScoreTextY))


#catch the snitch
def isHarryCatch(HarryX, HarryY, SnitchX, SnitchY):
    global Score
    global SnitchCounter
    global SnitchSpeed
    HarrySnitchDistance = math.sqrt((math.pow((HarryX + 40) - SnitchX, 2)) + (math.pow(HarryY - SnitchY, 2)))
    if HarrySnitchDistance < 50:
        SnitchCounter += SnitchSpeed + 1
        Score += 1
        SnitchSound.play()

    


# main music
mixer.music.load("Harry Potter Theme Song.wav")
mixer.music.play(-1)

#Bludger Hit Sound
BludgerSound = mixer.Sound("Harry Potter - Possession - HD (mp3cut.net).wav")

# Harry hurts
def isHarryHurts(HarryX,  HarryY, BludgerX, BludgerY):
    distance = math.sqrt((math.pow(HarryX - BludgerX, 2)) + (math.pow(HarryY - BludgerY, 2)))
    if distance < 50 :
        return True
    else:
        return False

#Health
Health_value = 3
font = pygame.font.Font('freesansbold.ttf', 38)
Health_textX = 966
Health_textY = 250

def showHealth(x, y):
    Health = font.render("Health : " + str(Health_value), True, (0, 0, 0))
    main_win.blit(Health, (x, y))

#game over

GameOverText = pygame.font.Font('freesansbold.ttf', 100)
GameOverTextX = 300
GameOverTextY = 260

def checkHealth(x, y):
    global DracoX
    global DracoY
    global borderCount
    global Health_textX
    global Health_textY
    global GameState
    global ScoreTextX
    global ScoreTextY
    global ScoreText
    if Health_value <= 0:
        GameState = False
        GameOverTextR = GameOverText.render("Game Over", True, (0, 0, 0))
        main_win.blit(GameOverTextR, (x, y))
        DracoX = 2000
        DracoY = 2000
        borderCount = 1070
        Health_textX = 2000
        Health_textY = 2000
        ScoreText = pygame.font.Font('freesansbold.ttf', 46)
        ScoreTextX = 475
        ScoreTextY = 400
    
timeShowBoost = random.randint(200, 250)
screenTime = 0
borderCount = 670

rectX = 300
rectY = 300
    #main loop

while running:
    main_win.blit(background, (0,0))

    #Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
    
    keys = pygame.key.get_pressed()
    # Harry Moves
    if keys[pygame.K_LEFT] and HarryX > 0:
        HarryX -= HarryVel
    if keys[pygame.K_RIGHT] and HarryX < borderCount:
        HarryX += HarryVel
    if keys[pygame.K_UP] and HarryY > 0:
        HarryY -= HarryVel
    if keys[pygame.K_DOWN] and HarryY < 575:
        HarryY += HarryVel

        
        
    # Draco Shots Bludger
    if Bludger_state == "ready":
            BludgerY = DracoY
            shotbludger(BludgerX, BludgerY)
    if BludgerX < 0:
        BludgerX = 700
        Bludger_state = "ready"
    if Bludger_state == "fire":
        shotbludger(BludgerX, BludgerY)
        BludgerX -= BludgerX_change

    # Draco Movement
    if DracoY >= 600 or isDown == True:
        isDown = True
        if DracoY >= 10:
            DracoY -= DracoVel
        else:
            isDown = False
    elif DracoY in range(0, 601):
        DracoY += DracoVel

    
    HarryHurts = isHarryHurts(HarryX, HarryY, BludgerX, BludgerY)
    if HarryHurts:
        BludgerSound.play()
        BludgerX = 700
        Bludger_state = "ready"
        Health_value -= 1

    showScore()
    if GameState is True:  
        isHarryCatch(HarryX, HarryY, SnitchX, SnitchY)

    checkHealth(GameOverTextX, GameOverTextY)
    # show images and update screen
    moveSnitch()
    showHealth(Health_textX, Health_textY)
    DracoFly()
    HarryFly()
    
    pygame.display.update()