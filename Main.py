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

bg = pygame.image.load('design/bg.jpg').convert()
bgMenu = pygame.image.load('design/bg_menu.jpg').convert()
bgRightPart = pygame.image.load('design/bgRightPart.png')
bgLeftPart = pygame.image.load('design/bgLeftPart.png')
mainFrame = pygame.image.load('design/mainFrame.png')
loadedPicture = pygame.image.load('1.jpg')

#

xStripe = 270
yStripe = 260
yFrame = 485
widthPhoto = 100
heightPhoto = 100
widthFrame = 110
heightFrame = 110
students_array = []

############################################################################################
############################################################################################
############################################################################################
############################################################################################

class Student():
    def __init__(self, name, id):
        self.picture = None
        self.name = name
        self.id = id
        self.picture_path = str(id)+'.jpg'

class Menu:
    def __init__(self, punkts = [120, 140, u'Game', (250, 250, 30), (250, 30, 250), 0]):
        self.punkts = punkts
    def render(self, screen, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                screen.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-30))
            else:
                screen.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-30))
    def menu(self):
        done = True
        pygame.mouse.set_visible(True)
        pygame.key.set_repeat(0,0)
        font_menu = pygame.font.Font('fonts/Peace Sans.otf', 100)
        punkt = 0
        while done:

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+690 and mp[1]>i[1] and mp[1]<i[1]+100:
                    punkt = i[5]
            self.render(bgMenu, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        if punkt == 0:
                            done = False
                        if punkt == 1:
                            sys.exit()
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    if punkt == 1:
                        sys.exit()

        #    window.blit(info_string, (0, 0))
            win.blit(bgMenu, (0,0))
            pygame.display.update()

####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

' создаем меню '
punkts = [(680, 470, u'Выбрать', (255, 255, 255), (0, 0, 0), 0),
          (600, 640, u'Присутствие', (255, 255, 255), (0, 0, 0), 1)]
game = Menu(punkts)
game.menu()


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
