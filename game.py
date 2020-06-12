import pygame
import sys
import random
import time
#
pygame.init()
win = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
#
pygame.display.set_caption("Randomizer")
#
xStripe = 270
yStripe = 260
yFrame = 485
widthPhoto = 100
heightPhoto = 100
widthFrame = 110
heightFrame = 110
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
mainFrame = pygame.image.load('design/mainFrame.png')
loadedPicture = pygame.image.load('1.jpg')
#
clock = pygame.time.Clock()
#
#
def drawWindow():
    global students_array
    global xStripe
    global iter
    global run
    win.blit(bg, (0,0))

    tStripe = xStripe

    for i in students_array:
        if (tStripe > 450 and tStripe < 650 and iter == 6):
            win.blit(loadedPicture, (t,yStripe,widthPhoto+100,heightPhoto+100))
            run = False
        else:
            win.blit(loadedPicture, (tStripe,yStripe,widthPhoto,heightPhoto))
        tStripe = tStripe + 230
        iter += 1

    win.blit(bgLeftPart,(0,0))
    win.blit(bgRightPart,(0,0))
    win.blit(mainFrame,(0,0))

    xStripe = xStripe - 1
    pygame.display.update()



run = True
for i in range(1,70):
    students_array.append(Student("Vanya", 1+i%4))
random.shuffle(students_array)


iter = 0
while run:
    # st = clock.get_time()
    clock.tick(60)
    # pygame.time.delay(1+iter)
    # print("ALL:", pygame.time.get_ticks())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawWindow()
    print("DRAW: ", clock.get_fps())
pygame.quit()
