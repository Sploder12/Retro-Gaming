import pygame
import sys
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Playin Like Its The 90s')
pygame.font.init()
pygame.key.set_repeat(1, 350) #when keys are held the event repeats after 350ms
myfont = pygame.font.SysFont('Consolas', 30) #font and font size HERE
#Held Key Delays
BLACK = (0,0,0)
DGRAY = (25,25,25)
GRAY = (50,50,50)
WHITE = (255,255,255)
screen.fill(BLACK)

running = True
games = open("projlist.txt","r") #gets the list of pyprojects
games1 = games.readlines()
for x in range(len(games1)):
        games1[x] = games1[x].rstrip() #removes pesky newlines

selected = 0
while(running): #the UI and Event Listeners, also sending data back to java
        screen.fill(BLACK)
        for event in pygame.event.get(): #Event Handling
                if (event.type == pygame.MOUSEBUTTONDOWN): 
                        running = False         #to replaced with JoyButtonDown
                        print("#RUN#"+games1[selected])
                        pygame.quit()
                        sys.exit()
                if (event.type == pygame.KEYDOWN): 
                        keys = pygame.key.get_pressed()
                        if (keys[pygame.K_UP]):#To be replaced with joyUp
                                if (selected <= 0):
                                        selected = len(games1)-1
                                else:
                                        selected -= 1
                        if (keys[pygame.K_DOWN]):#To be replaced with joyDown
                                if (selected >= len(games1)-1):
                                        selected = 0
                                else:
                                        selected += 1


        for y in range(len(games1)): #Drawing boxes around games
                if(y == selected):
                        pygame.draw.rect(screen,GRAY,(193,109+(50*y),1000,50))
                pygame.draw.rect(screen,WHITE,(193,109+(50*y),1000,50), 2)
                if(y != selected):
                        label = myfont.render(games1[y], 1, WHITE)
                        screen.blit(label, (200,120+(50*y)))
                else:
                        label = myfont.render(games1[y], 1, (0,225,0))
                        screen.blit(label, (200,120+(50*y)))
        pygame.display.update()        
games.close()
