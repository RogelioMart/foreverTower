import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()

winWidth = 800
winHeight = 447

win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('Forever Tower')

#you still don't hae a background image but just make a blue background like if it was a sky
#bg = pygame.image.load(os.path.join('assets','background.png')).convert()
#bgX = 0
#bgX2 = bg.get_width()

#you're not using a clock but just in case I copied this
#clock = pygame.time.Clock()

class saiphus(object):

    '''
    idler = [pygame.image.load(os.path.join('assets', 'adventurer-idle-00r.png')),
            pygame.image.load(os.path.join('assets', 'adventurer-idle-01r.png')),
            pygame.image.load(os.path.join('assets', 'adventurer-idle-02r.png'))]
    '''
    idler = [pygame.image.load(os.path.join('assets',  'adventurer-idle-0'+ str(x) + 'r' + '.png')) for x in range(0, 2)]
    runr = [pygame.image.load(os.path.join('assets','adventurer-run-00r.png')),
           pygame.image.load(os.path.join('assets','adventurer-run-01r.png')),
           pygame.image.load(os.path.join('assets','adventurer-run-02r.png')),
           pygame.image.load(os.path.join('assets','adventurer-run-03r.png'))]

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.idler = True
        self.idlerCnt = 0
        self.runr = False
        self.runrCnt = 0

    def draw(self, win):
        if self.runr:
            self.runrCnt = 0
            win.blit(self.runr[self.runrCnt], (self.x,self.y))
            self.runrCnt += 1
        else:
            if self.idlerCnt >24:
                self.idlerCnt = 0
            win.blit(self.idler[self.idlerCnt//16], (self.x, self.y))
            self.idlerCnt += 1

def updateScreen():
    chara.draw(win)
    
    pygame.display.update()

'''
MAIN
'''
idle = True
chara = saiphus(200, 313, 64, 64)
pause = 0
alive = True

while alive:
    '''
    if pause > 0:
        pause += 1
        if pause > fallSpeed * 2:
            endScreen()
    '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    if chara.idler == True:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            if not(chara.runr):
                chara.runr = True

    updateScreen()