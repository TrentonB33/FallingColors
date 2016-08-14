'''
Created on Jul 8, 2016

@author: TrentonB
'''
import pygame

class Meteor:
    '''
    Class of Meteors that generates on the main program
    '''

    def __init__(self, x, y, rad, color, xChng = 0, yChng = 0, xAccel=0, yAccel=0):
        
        self.x_coord = x
        self.y_coord = y
        self.radius = rad
        self.x_change = xChng
        self.y_change = yChng
        self.x_accel = xAccel
        self.y_accel = yAccel
        self.color = color
    
    def draw(self, gameScreen):
        '''temp functionality'''
        pygame.draw.circle(gameScreen, self.color, (self.x_coord,self.y_coord), self.radius)
        
    def doesIntersect(self, position, width=0, height=0):
        
        diam = self.radius*2
        
        check1 = position[0] >= self.x_coord and position[0] <= self.x_coord + diam
        check2 = position[0] + width >= self.x_coord and position[0] + width <= self.x_coord + diam
        check3 = position[1] >= self.y_coord and position[1] <= self.y_coord + diam
        check4 = position[1] + height >= self.y_coord and position[1] + height <= self.y_coord + diam
        
        return (check1 and check3) or (check1 and check4) or (check2 and check3) or (check2 and check4)
    
    def tick(self, gameSurface):
        
        self.x_change += self.x_accel
        self.y_change += self.y_accel
        self.x_coord += self.x_change
        self.y_coord += self.y_change
        return self.insideWindow(gameSurface)
        
    def insideWindow(self,gameSurface):
        
        surfaceDim = gameSurface.get_size()
        checkX = self.x_coord <= surfaceDim[0] + self.radius*2 and self.x_coord > 0 - self.radius*2
        checkY = self.y_coord <= surfaceDim[1] + self.radius*2
        
        return checkX and checkY
        
        
        
        
        
        