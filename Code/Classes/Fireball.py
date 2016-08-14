'''
Created on Aug 9, 2016

@author: TrentonB
'''
import pygame
from math import sqrt

class Fireball:
    '''
    Class for the fireball
    '''


    def __init__(self, StartX, StartY, DestX, DestY, Speed = 5):
        '''
        Constructor
        '''
        
        self.xPos = StartX
        self.yPos = StartY
        
        self.xStart = StartX
        self.yStart = StartY
        self.speed = Speed
        self.radius = 5
        
        xDif = DestX - self.xStart
        yDif = DestY - self.yStart
        trueSlope = yDif / xDif
        
        if(trueSlope > 0):
            self.direction = -1
        else:
            self.direction = 1
        
        
        #Check for divide by 0
        
        self.slope = abs(trueSlope)
        
        
        self.traveled = 0
        self.Dist = sqrt(pow(xDif, 2) + pow(yDif,2))
        
        
    
    def draw(self, gameScreen):
        pygame.draw.circle(gameScreen, (0,0,0), (self.xPos,self.yPos), self.radius)
        
    
    
    def tick(self, gameSurface):
        '''finish da distance formuler'''
        
        neum = pow(self.traveled,2)
        
        denom = pow(self.slope,2)+1
        
        xChange = sqrt(neum/denom)
        
        yChange = round(xChange * self.slope)
        xChange = round(xChange)
        
        self.xPos = self.xStart + self.direction * xChange
        self.yPos = self.yStart - yChange
        
        self.traveled += 5
        
        return self.insideWindow(gameSurface)
        
        
    def insideWindow(self,gameSurface):
        
        surfaceDim = gameSurface.get_size()
        checkX = self.xPos <= surfaceDim[0] + self.radius*2 and self.xPos > 0 - self.radius*2
        checkY = self.yPos > 0 - self.radius*2
        
        return checkX and checkY
    
    def getPos(self):
        return (self.xPos, self.yPos)
    
    def getRadius(self):
        return self.radius
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        