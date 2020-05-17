import pygame
import math
import random
from pygame import mixer
from tkinter.messagebox import showerror
running = False
DracoVel = None
SnitchSpeed = None
BludgerX_change = None

choice = int(input("What difficulty do you want to play? "))
if choice == 1:
    DracoVel = 4
    SnitchSpeed = 115
    BludgerX_change = 10
    running = True
elif choice == 2:
    DracoVel = 6
    BludgerX_change = 15
    SnitchSpeed = 100
    running = True
elif choice == 3:
    DracoVel = 8
    BludgerX_change = 20
    SnitchSpeed = 75
    running = True
elif choice == 4:
    DracoVel = 165
    BludgerX_change = 35
    SnitchSpeed = 45
    running = True
elif choice == 5:
    DracoVel = 30
    BludgerX_change = 45
    SnitchSpeed = 30
    running = True

pygame.init()
GameState = True
isDown = False
# window, caption, background
main_win = pygame.display.set_mode((1200, 750))
main_cap = pygame.display.set_caption("QUIDDITCH")
background = pygame.image.load("Quidditchpitch.png")

# Harry
HarryImage = pygame.image.load("harry-potter-quidditch-world-cup-broom-harry-potter-and-the-order-of-the-phoenix-harry-potter-png-clip-art.png")
HarryX = 100
HarryY = 150
HarryVel = 10

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
    

#not important but cool things
borderCount = 670

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
    if Bludger_state is "ready":
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