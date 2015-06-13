import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snakes")

clock = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None,25)

def snake(lead_x,lead_y,block_size):
    pygame.draw.rect(gameDisplay,green,[lead_x,lead_y,block_size,block_size]) #Coordinates of top left,width and height

def message_to_screen(msg,color):
    screen_text = font.render(msg,True,color)
    gameDisplay.blit(screen_text,[display_width/2,display_height/2])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-block_size)/10.0)*10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over,Press C to Continue/Q to Quit",black)
            pygame.display.update()

            for event in pygame.event.get():
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
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

            '''if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
            '''
        if lead_x > display_width or lead_x < 0 or lead_y > display_height or lead_y < 0:
            gameOver= True
        '''elif lead_x < 0:
            gameExit = True
        if lead_y > 600:
            gameExit = True
        elif lead_y < 0:
            gameExit = True'''

        lead_x += lead_x_change
        lead_y += lead_y_change

        '''if lead_x == 200 and lead_y == 200:
            print("Game's up! You WIN")
            pygame.quit()'''

        gameDisplay.fill(white)
        #gameDisplay.fill(red,rect=[200,200,block_size,block_size])
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,block_size,block_size])
        snake(lead_x,lead_y,block_size)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            '''message_to_screen("Yumm",green)
            pygame.display.update()'''
            randAppleX = round(random.randrange(0,display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0,display_height-block_size)/10.0)*10.0


        clock.tick(FPS)

    '''message_to_screen("You lose!",red)
    pygame.display.update()
    time.sleep(2)'''
    pygame.quit()
    quit()


gameLoop()

