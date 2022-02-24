import pygame # import pygame module 
pygame.init() # call the init function 

win = pygame.display.set_mode((800,700)) # create a tuple to make size of window

pygame.display.set_caption("2020 Revival") # when you open the game win the caption is called My first game

walkLeft = [pygame.image.load('Run (1).png'), pygame.image.load('Run (2).png'), pygame.image.load('Run (3).png'), pygame.image.load('Run (4).png'), pygame.image.load('Run (5).png'), pygame.image.load('Run (6).png'), pygame.image.load('Run (7).png'), pygame.image.load('Run (8).png'), pygame.image.load('Run (9).png')]
char = pygame.image.load('Walk (10).png')
bg = pygame.image.load('dumpsterfire.jpg')


x = 10
y = 30
width = 10
height = 15 # creating the size of my character
vel = 8 # speed or velocity of character
isJump = False 
jumpCount = 5
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 >=27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkcount//3],(x,y))
        walkCount += 1
    else :
        win.blit(char, (x,y))

    pygame.display.update()



run = True # created a run variable 
while run:
    pygame.time.delay(50)   # giving my loop a time delay / creating a clock 

    for event in pygame.event.get(): # create a for loop to check events
        if event.type == pygame.QUIT:  # if - for loop / if you type then the game will quit
            run = False
            
    keys = pygame.key.get_pressed() # this makes the shape (rectangle) move once the keys are pressed

     # These if statements will make our character move if these keys are pressed (up, down, right and left arrows
    if keys[pygame.K_LEFT]: 
        x-= vel    # we need to subtract to our x coordinates to move to the left
    if keys[pygame.K_RIGHT]:
        x+= vel    # we need to subtract to our x  coordinates to move to the left
    if keys[pygame.K_UP]:
        y-= vel     # we need to subtract to our y coordinates to move up
    if keys[pygame.K_DOWN]:
        y+= vel    # we need to subtract to our y coordinates to move  down
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False   
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

        redrawGameWindow()

    


pygame.quit()