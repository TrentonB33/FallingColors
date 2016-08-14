'''
Created on Jul 23, 2016

@author: TrentonB
'''

import pygame


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, x, y, wid, hght, spriteSheet = None, offset=None):
        '''
        Constructor
        '''
        
        self.xPos = x
        self.yPos = y
        self.width = wid
        self. height = hght
        
        if(offset == None):
            self.sprite = pygame.image.load(spriteSheet)
        