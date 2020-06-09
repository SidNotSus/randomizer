import pygame
import sys
import random
#
pygame.init()
win = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
#
pygame.display.set_caption("Randomizer")
#
xStripe = 270
yStripe = 260
xFrame = 805
yFrame = 485
widthPhoto = 100
heightPhoto = 100
widthFrame = 110
heightFrame = 110
animCount = 0
students_array = []
#
class Student():
    def __init__(self, name, id):
        self.picture = None
        self.name = name
        self.id = id
        self.picture_path = str(id)+'.jpg'
#
#
bg = pygame.image.load('design/bg.jpg').convert()
bgRightPart = pygame.image.load('design/bgRightPart.png')
bgLeftPart = pygame.image.load('design/bgLeftPart.png')
#
clock = pygame.time.Clock()
#
#
def drawWindow():
        global students_array
        global animCount
        global xStripe
        global xFrame
        global iter
        global run
        win.blit(bg, (0,0))
        if animCount + 1 >= 30:
            animCount = 0
        tStripe = xStripe
        tFrame = xFrame
        for i in students_array:
            #frame = pygame.image.load('design/frame.png').convert()
            mainFrame = pygame.image.load('design/mainFrame.png')
            loadedPicture = pygame.image.load(i.picture_path)
            if (tStripe > 450 and tStripe < 650 and iter == 6):
                win.blit(loadedPicture, (t,yStripe,widthPhoto+100,heightPhoto+100))
                run = False
            else:
                #win.blit(frame,(tFrame,yFrame,widthFrame,heightFrame))
                win.blit(loadedPicture, (tStripe,yStripe,widthPhoto,heightPhoto))
                win.blit(bgRightPart,(1660,0))
                win.blit(bgLeftPart,(0,0))

                win.blit(mainFrame,(0,0))
            tFrame = tFrame + 110
            tStripe = tStripe + 230
            iter += 1
        xStripe = xStripe - 1
        xFrame = xFrame - 1
        pygame.display.update()


run = True
for i in range(1,70):
    students_array.append(Student("Vanya", 1+i%4))
random.shuffle(students_array)
#

iter = 0
while run:
    clock.tick(600)
    pygame.time.delay(1+iter)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawWindow()
sleep(1000)
#
################################################################################
################################################################################
#
pygame.quit()
