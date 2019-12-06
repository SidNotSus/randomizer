import pygame

pygame.init()
win = pygame.display.set_mode((1466, 500))

pygame.display.set_caption("Randomizer")

#walkRigth = [pygame.image.load('right_1.png'),
#            pygame.image.load('right_2.png'),
#            pygame.image.load('right_3.png'),
#            pygame.image.load('right_4.png'),
#            pygame.image.load('right_5.png'),
#            pygame.image.load('right_6.png'),]
#walkLeft = [pygame.image.load('left_1.png'),
#            pygame.image.load('left_2.png'),
#            pygame.image.load('left_3.png'),
#            pygame.image.load('left_4.png'),
#            pygame.image.load('left_5.png'),
#            pygame.image.load('left_6.png'),]

bg = pygame.image.load('bg.jpg')
playerStand = pygame.image.load('idle.png')

clock = pygame.time.Clock()


x=50
y=420
width = 60
height = 71
speed = 10


isJump=False
jumpCount = 10

left = False
rigth = False
animCount = 10



def drawWindow():
        count = 0
        global animCount
        win.blit(bg, (0,0))

#        if left:
#            win.blit(walkLeft[animCount // 5], (x,y))
#            animCount +=1


#       win.blit(playerStand, (x,y))

        while count > 10:
            pygame.draw.rect(win,(0,0,255),(x,y,width,height))
            x+=20
            count=count+1
            if x > 150:
                break
        pygame.display.update()


################################################################################
######################################GAME######################################
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

    if keys[pygame.K_SPACE]:
        for i in range(20):
                x-=speed
                left = True
                rigth = False

    drawWindow()

################################################################################
################################################################################

pygame.quit()
