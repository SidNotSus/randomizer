import pygame

pygame.init()
win = pygame.display.set_mode((1466, 500))

pygame.display.set_caption("Randomizer")

walkRigth = [pygame.image.load('right_1.png'),
            pygame.image.load('right_2.png'),
            pygame.image.load('right_3.png'),
            pygame.image.load('right_4.png'),
            pygame.image.load('right_5.png'),
            pygame.image.load('right_6.png'),]
walkLeft = [pygame.image.load('left_1.png'),
            pygame.image.load('left_2.png'),
            pygame.image.load('left_3.png'),
            pygame.image.load('left_4.png'),
            pygame.image.load('left_5.png'),
            pygame.image.load('left_6.png'),]

bg = pygame.image.load('bg.jpg')
playerStand = pygame.image.load('idle.png')

clock = pygame.time.Clock()


x=50
y=380
width = 51
height = 120
speed = 10

isJump=False
jumpCount = 10

left = False
rigth = False
animCount = 0



def drawWindow():
        global animCount
        win.blit(bg, (0,0))
        if animCount + 1 >= 30:
            animCount = 0

        if left:
            win.blit(walkLeft[animCount // 5], (x,y))
            animCount +=1
        elif rigth:
            win.blit(walkRigth[animCount // 5], (x,y))
            animCount +=1
        else:
            win.blit(playerStand, (x,y))

        #pygame.draw.rect(win,(0,0,255),(x,y,width,height))
        pygame.display.update()

#        win.blit(bg, (0,0))
#
#        win.blit(playerStand, (x,y))
#
#    #    pygame.draw.rect(win,(0,0,255),(x,y,width,height))
#        pygame.display.update()


################################################################################
########################################GAME####################################
run = True
while run:
    clock.tick(30)
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and x<1466 - width - 5:
        for i in range(20):
            if x<1466 - width - 5:
                x+=speed
                left = True
                rigth = False
    elif keys[pygame.K_a] and x>5:
        for i in range(20):
            if  x>5:
                x-=speed
                left = True
                rigth = False
    if keys[pygame.K_LEFT] and x>5:
        x-= speed
        left = True
        rigth = False
    elif keys[pygame.K_RIGHT] and x<1466 - width - 5:
        x+= speed
        left = False
        rigth = True
    else:
        left = False
        rigth = False
        animCount = 0

    if not (isJump):
        if keys[pygame.K_SPACE]:
                isJump = True

    else:
    #    for i in range(20):
            if jumpCount >= -10:
                if jumpCount < 0:
                    x+=(jumpCount ** 2) / 2
                else:
                    x-=(jumpCount ** 2) / 2
                    jumpCount -= 1
            else:
                    isJump=False
                    jumpCount=10
    drawWindow()

################################################################################
################################################################################

pygame.quit()
