import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
light_red = (180,0,0)
green = (37,177,28)
light_green = (0,255,0)
blue = (0,0,255)
yellow = (200,100,0)
light_yellow = (200,50,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tanks")

'''img = pygame.image.load('head2.png')
appleimg = pygame.image.load('apple2.png')
icon = pygame.image.load('apple2.png')
pygame.display.set_icon(icon)'''

clock = pygame.time.Clock()

tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWIdth = 5

smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",80)

def pause():
    paused = True

    message_to_screen("Paused",black,-100,"large")
    message_to_screen("Press C to continue or Q to quit",black,25)

    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)


def score(score):
    text = smallfont.render("Score: "+ str(score),True,black)
    gameDisplay.blit(text,[0,0])


def tank(x,y,turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x-20,y-2),(x-19,y-5),(x-18,y-8),(x-17,y-11),(x-16,y-14),(x-15,y-17),(x-14,y-20),(x-13,y-23),(x-12,y-26)]

    pygame.draw.circle(gameDisplay,blue,(x,y),int(tankHeight/2))
    pygame.draw.rect(gameDisplay,blue,(x-tankHeight,y,tankWidth,tankHeight))

    pygame.draw.line(gameDisplay,blue,(x,y),possibleTurrets[turPos],turretWidth)

    startX = 20

    for i in range(8):
        pygame.draw.circle(gameDisplay,blue,(x-startX,y+20),wheelWIdth)
        startX -= 5

    return possibleTurrets[turPos]

def game_controls():

    gCont = True

    while gCont:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Controls",green,-100,"large")
        message_to_screen("Fire : Spacebar",black,-30,"small")
        message_to_screen("Control turret : Up and Down arrows",black,10,"small")
        message_to_screen("Control tanks : Left and Right arrows",black,50,"small")
        message_to_screen("Pause : P ",black,90,"small")

        cur = pygame.mouse.get_pos()

        button("Play",150,500,100,50,green,light_green,action="play")
        button("Menu",350,500,100,50,yellow,light_yellow,action="main")
        button("Quit",550,500,100,50,red,light_red,action="quit")

        pygame.display.update()
        clock.tick(15)


def button(text,x,y,wd,ht,inactive_color,active_color,action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+wd > cur[0] > x and y+ht > cur[1] > y :
        pygame.draw.rect(gameDisplay,active_color,(x,y,wd,ht))

        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action == "play":
                gameLoop()
            if action == "main":
                game_intro()

    else:
        pygame.draw.rect(gameDisplay,inactive_color,(x,y,wd,ht))

    text_to_button(text,black,x,y,wd,ht)

def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks",green,-100,"large")
        message_to_screen("The objective is to shoot & destroy",black,-30,"small")
        message_to_screen("the enemy tank before they destroy you",black,10,"small")
        message_to_screen("The more enemies you destroy the harder they get",black,50,"small")

        cur = pygame.mouse.get_pos()

        button("Play",150,500,100,50,green,light_green,action="play")
        button("Controls",350,500,100,50,yellow,light_yellow,action="controls")
        button("Quit",550,500,100,50,red,light_red,action="quit")

        pygame.display.update()
        clock.tick(15)

def text_objects(text,color,size):

    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = medfont.render(text,True,color)
    if size == "large":
        textSurface = largefont.render(text,True,color)

    return textSurface,textSurface.get_rect()

def text_to_button(text,color,buttonx,buttony,buttonwid,buttonht,size="small"):
    textSurf,textRect = text_objects(text,color,size)
    textRect.center = ((buttonx+(buttonwid/2)),buttony+(buttonht/2))
    gameDisplay.blit(textSurf,textRect)

def message_to_screen(msg,color,y_displace=0,size = "small"):

    textSurf,textRect = text_objects(msg,color,size)
    textRect.center =(int ( display_width/2 )), (int(display_height/2))+y_displace
    gameDisplay.blit(textSurf,textRect)

def barrier(xLocation,randomHeight,barrierWidth):
    pygame.draw.rect(gameDisplay,black,[xLocation, display_height-randomHeight , barrierWidth , randomHeight])

'''def fireShell(xy,tankX,tankY,turPos,gunPower):

    fire = True
    startingShell = list(xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay,red,(startingShell[0],startingShell[1]),5)
        startingShell[0] -= (12-turPos)*2
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015)**2) - (turPos + turPos/(12-turPos)))

        if startingShell[1] > display_height:
            fire = False

        pygame.display.update()
        clock.tick(60)'''

def fireShell(xy,tankX,tankY,turPos,gunPower):

    fire = True
    startingShell = list(xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.circle(gameDisplay,green,(startingShell[0],startingShell[1]),5)
        startingShell[0] -= (12-turPos)*2
        startingShell[1] += int((((startingShell[0]-xy[0])*0.015/(gunPower/50))**2) - (turPos + turPos/(12-turPos)))

        if startingShell[1] > display_height:
            fire = False

        pygame.display.update()
        clock.tick(60)

def power(level):
    text = smallfont.render("Power : "+str(level)+"%",True,black)
    gameDisplay.blit(text,[display_width/2,0])



def gameLoop():

    gameExit = False
    gameOver = False
    FPS = 15
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0

    barrierWidth = 50

    curTurPos = 0
    changeTur = 0

    firePower = 50
    powerChange = 0

    xLocation = (display_width/2) + random.randint(-0.2*display_width , 0.2*display_width)
    randomHeight = random.randrange(0.1*display_height , 0.6*display_height)

    while not gameExit:

        gameDisplay.fill(white)
        gun = tank(mainTankX,mainTankY,curTurPos)

        if gameOver == True:
            message_to_screen("Game over",black,-50,size = "large")
            message_to_screen("Press C to Continue or Q to Quit",red,50,size = "medium")
            pygame.display.update()

        while gameOver == True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                elif event.key == pygame.K_UP:
                    changeTur = 1
                elif event.key == pygame.K_DOWN:
                    changeTur = -1
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_SPACE:
                    fireShell(gun,mainTankX,mainTankY,curTurPos,firePower)
                    #fireShell2(gun,mainTankX,mainTankY,curTurPos,firePower)

                elif event.key == pygame.K_a:
                    powerChange = -1
                elif event.key == pygame.K_d:
                    powerChange = 1


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    powerChange = 0

        mainTankX += tankMove
        curTurPos += changeTur

        if curTurPos > 8:
            curTurPos = 8
        elif curTurPos < 0:
            curTurPos = 0

        if mainTankX - (tankWidth/2) < xLocation + barrierWidth:
            mainTankX += 5

        firePower += powerChange
        power(firePower)

        for x in range(1):
            barrier(xLocation,randomHeight,barrierWidth)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()


