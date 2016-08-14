import pygame
from Classes.Meteor import Meteor
from Classes.Fireball import Fireball
from random import randint, gauss
'''
Author: Trenton Baldrey
'''

#Initialize Pygame
pygame.init()

'''
******************************************************
*GLOBAL VARIABLES                                    *
******************************************************
'''

colors = []

colors.append((0,0,0))
colors.append((100,30,200))
colors.append((255,0,0))
colors.append((0,255,0))
colors.append((0,0,255))

#Set the needed variables for creating the Pygame surface
winWidth = 1280
winHeight = 800

gameSurface = pygame.display.set_mode((winWidth,winHeight))
pygame.display.set_caption("Falling Colors")

#Get a game clock
gameClock = pygame.time.Clock()
framerate = 30

#Meteor variables
numMeteors = 30
remainingMeteors = 30;
numToGen = 0
Meteors = []
variation = 5
radius = 20

#Fireballs
Fireballs = []

#House
houseImg = pygame.image.load('../resources/House.png')

def calculateXChange(xpos,yChng):
    mean = winWidth/2
    #stdDev = 1
    stdDev = winWidth/6
    xDest = gauss(mean, stdDev)
    xDif = xDest - xpos
    
    yTime = winHeight/yChng
    
    xChange = xDif/yTime
    
    return round(xChange)
    

def drawHouse():
    gameSurface.blit(houseImg, (winWidth/2-25,winHeight-50))

def checkMousePos():
    
    mousePos = pygame.mouse.get_pos()
    
    for Meteor in Meteors:
        if Meteor.doesIntersect(mousePos):
            Meteors.remove(Meteor)


#Function declarations
def genMeteors():
    
    if len(Meteors) < numMeteors:
            
            remainingMeteors = numMeteors - len(Meteors)
            numToGen = randint(0, remainingMeteors)
            
            for i in range(0,numToGen):
                
                xPos = randint(0, winWidth)
                yChange = randint(1,variation)
                xChange = calculateXChange(xPos,yChange)
                
                metColor = colors[randint(0, len(colors)-1)]
                
                Meteors.append(Meteor(xPos, 0, radius, metColor, xChange, yChange))
                #Meteors[i].draw(gameSurface)

def refreshMeteors():
    inBound = True
    itr = 0
    while itr < len(Meteors):
        
        inBound = Meteors[itr].tick(gameSurface)
        Meteors[itr].draw(gameSurface)
        
        if not inBound:
            Meteors.pop(itr)
        else:
            itr+=1
            
def refreshFireballs():
    inBound = True
    itr = 0
    while itr < len(Fireballs):
        
        inBound = Fireballs[itr].tick(gameSurface)
        
        Fireballs[itr].draw(gameSurface)
        
        if not inBound:
            Fireballs.pop(itr)
        else:
            itr+=1
            
    
def detectFireballCollision():
    
    mets = 0
    fires = 0
    
    while mets < len(Meteors):
        currentMet = Meteors[mets]
        fires = 0
        while fires < len(Fireballs):
            curFire = Fireballs[fires]
            curRad = curFire.getRadius()
            if( currentMet.doesIntersect( curFire.getPos(), curRad, curRad )):
                Meteors.pop(mets)
                Fireballs.pop(fires)
            
            fires += 1
        mets += 1
    
            

def startGame():
    
    active=True
    
    while(active):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if(event.button == 1):
                    tempFire = Fireball(winWidth//2, winHeight, event.pos[0], event.pos[1])
                    Fireballs.append(tempFire)
                
                        
        genMeteors()
        
        #checkMousePos()                
        
        gameSurface.fill((255,255,255))
        
        drawHouse()
        
        refreshMeteors()
        
        refreshFireballs()
        
        detectFireballCollision()
            
        pygame.display.update()
            
        gameClock.tick(framerate)
    
    return

'''
Actual start of the code
'''


startGame()
    
pygame.quit()
quit()



