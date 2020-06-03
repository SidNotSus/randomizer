import pygame
import sys
import random
#
pygame.init()
win = pygame.display.set_mode((1466, 500))
#
pygame.display.set_caption("Randomizer")
#
xStripe = 700
yStripe = 200
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
bg = pygame.image.load('bg.jpg')
#
clock = pygame.time.Clock()
#
#
def drawWindow():
        global students_array
        global animCount
        global xStripe
        global iter
        global run
        win.blit(bg, (0,0))
        if animCount + 1 >= 30:
            animCount = 0
        t = xStripe
        for i in students_array:
            frame = pygame.image.load('frame.jpg')
            loadedPicture = pygame.image.load(i.picture_path)
            if (t > 450 and t < 650 and iter == 6):
                win.blit(loadedPicture, (t,yStripe,widthPhoto+100,heightPhoto+100))
                run = False
            else:
                win.blit(frame,(t,yStripe,widthFrame,heightFrame))
                win.blit(loadedPicture, (t,yStripe,widthPhoto,heightPhoto))
            t = t + 110
            iter += 1
        xStripe = xStripe - 1
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
