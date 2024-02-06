import pygame
import sys
import random
import math

pygame.init()
display = pygame.display.set_mode((1500, 800))

#Animations of the Character
R_Standing = pygame.image.load("Character3.png")
L_Standing = pygame.image.load("Character5.png")
R_Walking = pygame.image.load("Character2.png")
L_Walking = pygame.image.load("Character6.png")
BulletLeft = pygame.image.load("BulletLeft.png")
BulletRight = pygame.image.load("BulletRight.png")
LongBlock = pygame.image.load("LongBlock.png")
MediumBlock = pygame.image.load("MediumBlock.png")
MiddleBlock = pygame.image.load("MiddleBlock.png")
ShortBlock = pygame.image.load("ShortBlock.png")
Floor = pygame.image.load("Grass.png")
Cloud = pygame.image.load("Cloud1.png")
Enemy_S = pygame.image.load("EnemyIdle.png")
Enemy_ML = pygame.image.load("EnemyMove.png")
Enemy_MR = pygame.transform.flip(Enemy_ML, True, False)
Enemy_WR = pygame.image.load("EnemyWalk.png")
Enemy_WL = pygame.transform.flip(Enemy_WR, True, False)
Walking_Right = [R_Standing, R_Walking, R_Standing]
Walking_Left = [L_Standing, L_Walking, L_Standing]
Standing = R_Standing
Character = Standing
#Start menu and scorekeeper
Starting = True
sound = pygame.mixer.Sound("Testing.mp3")

#Character Jumping and Movement Variables
jump = False
jumpCount = 10
LeftorRight = False
vel = 4
sleeptime = 10
x = 75
y = 690
realy = 0
width = Standing.get_width()
height = Standing.get_height()
gravity = False
scroll = False
val = 0

#Text Section
hp_level = 100
font = pygame.font.SysFont('Comic Sans MS', 20)
Font = pygame.font.SysFont('Comic Sans MS', 32)
Startbutton = Font.render("Start", True, (255, 255, 255))
Exitbutton = Font.render("Exit", True, (255, 255, 255))
b1 = font.render("Block1", True, (255, 255,255))
b2 = font.render("Block2", True, (255, 255,255))
b3 = font.render("Block3", True, (255, 255,255))
b4 = font.render("Block4", True, (255, 255,255))
b5 = font.render("Block5", True, (255, 255,255))
b6 = font.render("Block6", True, (255, 255,255))
HP_BAR = font.render("HP Bar", True, (255, 255, 255))
fontGO = pygame.font.SysFont("Comic Sans Ms", 1200, True)
GameOver = font.render("GAME OVER", True, (255, 255, 255))
C_Meter = 0
score = 0
meterScore = []
Meters = font.render(f'Meters: {C_Meter}', True, (0, 0, 0))
Stuff = font.render("Press the Button", True, (0,0,0))
#Bullet Variables
bx = 1500
by = y
Bullet = BulletRight
bvel = 9
shot = False

#Block designing and variables
Block_width = {
    LongBlock : 225,
    MediumBlock : 175, 
    MiddleBlock : 100,
    ShortBlock : 60
}
blockType = [ShortBlock, MiddleBlock, MediumBlock, LongBlock]
blockSide = ["left", "right"]
Floory = 750
Block1x = 825
Block1y = 600
Block2x = 40
Block2y = 40
Block3x = 40
Block3y = 40
Block4x = 40
Block4y = 40
Block5x = 40
Block5y = 40
Block6x = 40
Block6y = 40
Block7x = 40
Block7y = 40
Block2 = random.choice(blockType)
Block1 = random.choice(blockType)
Block3 = random.choice(blockType)
Block4 = random.choice(blockType)
Block5 = random.choice(blockType)
Block6 = random.choice(blockType)
Block7 = random.choice(blockType)
Blocks = [Block1, Block2, Block3, Block4, Block5, Block6]
lastBlock = "Block1"
resetting = False

#Collision Detection
C_Mask = pygame.mask.from_surface(Standing)
Bullet_mask = pygame.mask.from_surface(Bullet)
Block1_mask = pygame.mask.from_surface(Block1)
Block2_mask = pygame.mask.from_surface(Block2)
Block3_mask = pygame.mask.from_surface(Block3)
Block4_mask = pygame.mask.from_surface(Block4)
Block5_mask = pygame.mask.from_surface(Block5)
Block6_mask = pygame.mask.from_surface(Block6)
Block7_mask = pygame.mask.from_surface(Block7)

#Enemy for 100m
Enemy1 = True
Enemy2 = False
Enemy3 = False
Enemy4 = False
enemy1x = 0
enemy1y = 0
enemy2x = 0
enemy2y = 0
enemy3x = 0
enemy3y = 0
enemy4x = 0
enemy4y = 0
enemies = [Enemy1, Enemy2, Enemy3, Enemy4]
EnemyX = {
    Enemy1 : enemy1x,
    Enemy2 : enemy2x,
    Enemy3 : enemy3x,
    Enemy4 : enemy4x
}
EnemyY = {
    Enemy1 : enemy1y,
    Enemy2 : enemy2y,
    Enemy3 : enemy3y,
    Enemy4 : enemy4y
}
idle1 = True
idle2 = True
idle3 = True
idle4 = True
ENEMY1 = Enemy_S
enemy_mask = pygame.mask.from_surface(ENEMY1)
Evel = 2

#Testing section
respawn = False

#Game Over section
gameOver = True

while True:
    
    pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            pygame.quit()    
            sys.exit()

    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
    
    if pygame.mouse.get_pressed()[0] == True:
        sound.play()
        if pos[0] > 500 and pos[0] < 625 and pos[1] > 360 and pos[1] < 440:
            Starting = False
            gameOver = True
            hp_level = 100
            lastBlock = 'Block1'
            Block1x = 825
            Block1y = 600
            x = 75
            y = 690
            Floory = 760
            scroll = False
        elif pos[0] > 800 and pos[0] < 925 and pos[1] > 360 and pos[1] < 440:
            pygame.quit()
            sys.exit()
    
    display.fill((74, 174, 240))
    pygame.draw.rect(display, (90, 214, 55), (500, 360, 125, 80))
    pygame.draw.rect(display, (255, 255, 255), (500, 360, 125, 80), 4)
    pygame.draw.rect(display, (235, 51, 36), (800, 360, 125, 80))
    pygame.draw.rect(display, (255, 255, 255), (800, 360, 125, 80), 4)
    display.blit(Startbutton, (520, 380))
    display.blit(Exitbutton, (825, 378))
    pygame.time.delay(10)
    pygame.display.update()

    while gameOver and not Starting:
        #keep the game running 
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if pygame.event == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()
            
        display.fill((74, 174, 240))
        #Block positioning and creation
        if lastBlock == 'Block1':
            if Block2y > 850 or not scroll or resetting:
                lastBlock = "Block2"
                Block2 = random.choice(blockType)
                BLOCK = random.choice(blockSide)
                if BLOCK == 'left' and Block1x < 100:
                    BLOCK = 'right'
                elif BLOCK == 'right' and Block1x + Block_width.get(Block1) > 1375:
                    BLOCK = 'left'
                if BLOCK == 'left':
                    Block2x = random.randint(Block1x - 170 - Block_width.get(Block2), Block1x - 100 - Block_width.get(Block2))
                    Block2y = random.randint(Block1y - 180, Block1y - 140)
                elif BLOCK == 'right':
                    Block2x = random.randint(Block1x + 100 + Block_width.get(Block1), Block1x + 170 + Block_width.get(Block1))
                    Block2y = random.randint(Block1y - 180, Block1y - 140)
                if Block2x < 0 or Block2x + Block_width.get(Block2) > 1495:
                    lastBlock = 'Block1'
                    print("hi")
                    resetting = True
                else:
                    lastBlock = 'Block2'
                    resetting = False
        elif lastBlock == 'Block2': 
            if not scroll or Block3y > 850 or resetting:
                lastBlock = "Block3"
                Block3 = random.choice(blockType)
                if BLOCK == 'left' and Block2x < 100:
                    BLOCK = 'right'
                elif BLOCK == 'right' and Block2x + Block_width.get(Block2) > 1375:
                    BLOCK = 'left'
                BLOCK = random.choice(blockSide)
                if BLOCK == 'left':
                    Block3x = random.randint(Block2x - 170 - Block_width.get(Block3), Block2x - 100 - Block_width.get(Block3))
                    Block3y = random.randint(Block2y - 180, Block2y - 140)
                elif BLOCK == 'right':
                    Block3x = random.randint(Block2x + 100 + Block_width.get(Block2), Block2x + 170 + Block_width.get(Block2))
                    Block3y = random.randint(Block2y - 180, Block2y - 140)
                if Block3x < 0 or Block3x + Block_width.get(Block3) > 1495:
                    lastBlock = 'Block2'
                    print("hi")
                    resetting = True
                else:
                    lastBlock = 'Block3'
                    resetting = False
        elif lastBlock == 'Block3':
            if not scroll or Block4y > 850 or resetting:
                lastBlock = "Block4"
                Block4 = random.choice(blockType)
                BLOCK = random.choice(blockSide)
                if BLOCK == 'left' and Block3x < 100:
                    BLOCK = 'right'
                elif BLOCK == 'right' and Block3x + Block_width.get(Block3) > 1375:
                    BLOCK = 'left'
                if BLOCK == 'left':
                    Block4x = random.randint(Block3x - 170 - Block_width.get(Block4), Block3x - 100 - Block_width.get(Block4))
                    Block4y = random.randint(Block3y - 180, Block3y - 140)

                elif BLOCK == 'right':
                    Block4x = random.randint(Block3x + 100 + Block_width.get(Block3), Block3x + 170 + Block_width.get(Block3))
                    Block4y = random.randint(Block3y - 180, Block3y - 140)
                if Block4x < 0 or Block4x + Block_width.get(Block4) > 1495:
                    lastBlock = 'Block3'
                    print("hi")
                    resetting = True
                else:
                    lastBlock = 'Block4'
                    resetting = False
        elif lastBlock == 'Block4':
            if not scroll or Block5y > 850 or resetting:
                lastBlock = "Block5"
                Block5 = random.choice(blockType)
                BLOCK = random.choice(blockSide)
                if BLOCK == 'left' and Block4x < 100:
                    BLOCK = 'right'
                elif BLOCK == 'right' and Block4x + Block_width.get(Block4) > 1375:
                    BLOCK = 'left'
                if BLOCK == 'left':
                    Block5x = random.randint(Block4x - 170 - Block_width.get(Block5), Block4x - 100 - Block_width.get(Block5))
                    Block5y = random.randint(Block4y - 180, Block4y - 140)

                elif BLOCK == 'right':
                    Block5x = random.randint(Block4x + 100 + Block_width.get(Block4), Block4x + 170 + Block_width.get(Block4))
                    Block5y = random.randint(Block4y - 180, Block4y - 140)
                if Block5x < 0 or Block5x + Block_width.get(Block5) > 1495:
                    lastBlock = 'Block4'
                    print("hi")
                    resetting = True
                else:
                    lastBlock = 'Block5'
                    resetting = False
        elif lastBlock == 'Block5':
            if not scroll or Block6y > 850 or resetting:
                lastBlock = "Block6"
                Block6 = random.choice(blockType)
                BLOCK = random.choice(blockSide)
                if BLOCK == 'left' and Block5x < 100:
                    BLOCK = 'right'
                elif BLOCK == 'right' and Block5x + Block_width.get(Block5) > 1375 :
                    BLOCK = 'left'
                if BLOCK == 'left':
                    Block6x = random.randint(Block5x - 170 - Block_width.get(Block6), Block5x - 100 - Block_width.get(Block6))
                    Block6y = random.randint(Block5y - 180, Block5y - 140)

                elif BLOCK == 'right':
                    Block6x = random.randint(Block5x + 100 + Block_width.get(Block5), Block5x + 170 + Block_width.get(Block5))
                    Block6y = random.randint(Block5y - 180, Block5y - 140)
                if Block6x < 0 or Block6x + Block_width.get(Block6) > 1495:
                    lastBlock = 'Block5'
                    print("hi")
                    resetting = True
                else:
                    lastBlock = 'Block6'
                    resetting = False
        elif lastBlock == 'Block6':
            if not scroll or Block7y > 850 or resetting:
                lastBlock = "Block7"
                Block7 = random.choice(blockType)
                BLOCK = random.choice(blockSide)
                if BLOCK == 'left' and Block6x < 100:
                    BLOCK = 'right'
                elif BLOCK == 'right' and Block6x + Block_width.get(Block6) > 1375 :
                    BLOCK = 'left'
                if BLOCK == 'left':
                    Block7x = random.randint(Block6x - 170 - Block_width.get(Block1), Block6x - 100 - Block_width.get(Block1))
                    Block7y = random.randint(Block6y - 180, Block6y - 140)

                elif BLOCK == 'right':
                    Block7x = random.randint(Block6x + 100 + Block_width.get(Block6), Block6x + 170 + Block_width.get(Block6))
                    Block7y = random.randint(Block6y - 180, Block6y - 140)
                if Block7x < 0 or Block7x + Block_width.get(Block7) > 1495:
                    lastBlock = 'Block6'
                    print("hi")
                    resetting = True
                else:
                    lastBlock = 'Block7'
                    resetting = False
        
        elif lastBlock == 'Block7':
            if Block1y > 850 or resetting:
                lastBlock = "Block1"
                Block1 = random.choice(blockType)
                BLOCK = random.choice(blockSide)
                if BLOCK == 'left' and Block7x < 100:
                    BLOCK = 'right'
                elif BLOCK == 'right' and Block7x + Block_width.get(Block7) > 1375 :
                    BLOCK = 'left'
                if BLOCK == 'left':
                    Block1x = random.randint(Block7x - 150 - Block_width.get(Block1), Block7x - 100 - Block_width.get(Block1))
                    Block1y = random.randint(Block7y - 180, Block7y - 140)

                elif BLOCK == 'right':
                    Block1x = random.randint(Block7x + 100 + Block_width.get(Block7), Block7x + 170 + Block_width.get(Block7))
                    Block1y = random.randint(Block7y - 180, Block7y - 140)
                if Block1x < 0 or Block1x + Block_width.get(Block1) > 1495:
                    lastBlock = 'Block7'
                    print("hi")
                    resetting = True
                else:
                    lastBlock = 'Block1'
                    resetting = False
        
        Block1_mask = pygame.mask.from_surface(Block1)
        Block2_mask = pygame.mask.from_surface(Block2)
        Block3_mask = pygame.mask.from_surface(Block3)
        Block4_mask = pygame.mask.from_surface(Block4)
        Block5_mask = pygame.mask.from_surface(Block5)
        Block6_mask = pygame.mask.from_surface(Block6)
        Block7_mask = pygame.mask.from_surface(Block7)

        #enemy positioning
        for i in enemies:
            if i:
                enemy1x = Block1x + (Block_width.get(Block1)//2) - 20
                if idle1:
                    enemy1y = Block1y - 40
                    ENEMY1 = Enemy_S
                else:
                    enemy1y = Block1y - 54
                    ENEMY1 = Enemy_ML
                    enemy1x -= Evel
                    if enemy1x < Block1x:
                        enemy1x = Block1x
            else:
                if not Enemy1:
                    enemy1x = -40
                    enemy1y = 802
        
        if Bullet_mask.overlap(enemy_mask, (enemy1x - bx, enemy1y - by)):
            Enemy1 = False
        if Block1y < 0 and not Enemy1:
            Enemy1 = True
        
        #player movement 
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if x < 5:
                x = 7
                hp_level -= 1
            else:
                Standing = L_Standing
                LeftorRight = True
                x -= vel
                if val//5 >= len(Walking_Left):
                    val = 0
                Character = Walking_Left[val//5]
                val += 1
                if enemy_mask.overlap(C_Mask, (x - enemy1x, y - enemy1y)):
                    hp_level -= 5
                    x += 10
        
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if x > 1445:
                x = 1443
                hp_level -= 1
            else:
                LeftorRight = False
                Standing = R_Standing
                x += vel
                if val//5 >= len(Walking_Right):
                    val = 0
                Character = Walking_Right[val//5]
                val += 1
                if enemy_mask.overlap(C_Mask, (x - enemy1x, y - enemy1y)):
                    hp_level -= 5
                    x -= 7
        
        if jump:
            
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                realy += (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1
                vel = 10
                sleeptime = 25
                if LeftorRight:
                    Character = L_Standing
                else:
                    Character = R_Standing
            else:
                jump = False
                jumpCount = 10
                sleeptime = 10
                vel = 4
        else:
            if not C_Mask.overlap(Block1_mask, (Block1x - x, Block1y - y - 10)) and not C_Mask.overlap(Block2_mask, (Block2x - x, Block2y - y - 10)) and not C_Mask.overlap(Block4_mask, (Block4x - x, Block4y - y - 10)) and not C_Mask.overlap(Block3_mask, (Block3x - x, Block3y - y - 10)) and not C_Mask.overlap(Block5_mask, (Block5x - x, Block5y - y - 10)) and not C_Mask.overlap(Block6_mask, (Block6x - x, Block6y - y - 10)) and not C_Mask.overlap(Block7_mask, (Block7x - x, Block7y - y - 10)) and y < 683:
                y += 11
            else: 
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    jump = True
        
        if keys[pygame.K_DOWN]:
            y = 700
            realy = 0

        #Camera rolling 
        if y <= 225:
            scroll = True
            Floory += vel
            Block1y += vel
            Block2y += vel
            Block3y += vel
            Block4y += vel
            Block5y += vel
            Block6y += vel
            Block7y += vel
        
        elif scroll and y >= 683:
            jump = False
            if LeftorRight:
                    Character = L_Standing
            else:
                Character = R_Standing
            if Floory > 760:
                Floory -= vel * 3
                Block1y -= vel * 3
                Block2y -= vel * 3
                Block3y -= vel * 3
                Block4y -= vel * 3
                Block5y -= vel * 3
                Block6y -= vel*3
                Block7y -= vel*3
            else:
                scroll = False

        if not scroll and Floory - Block1y > 500:
            x = Block1x + 10
            y = Block1y - 10
            Floory += vel*20
            Block1y += vel*20
            Block2y += vel*20
            Block3y += vel*20
            Block4y += vel*20
            Block5y += vel*20
            Block6y += vel*20
            Block7y += vel*20
            respawn = True

        if respawn and y < 9:
            ResPawn = Font.render("RESPAWNING...", True, (255, 255, 255))
            display.blit(ResPawn, (700, 362))
        else:
            respwan = False

        if y < 10:
            jumpCount = -11

        #Collision detection
        if C_Mask.overlap(Block1_mask, (Block1x - x, Block1y - y)):
            if x + width > Block1x and x < Block1x + Block_width.get(Block1):
                if y > Block1y + 7:
                    y = Block1y + 50
                    jumpCount = -11
                if y - 20 < Block1y:
                    idle1 = False
                    y = Block1y - height
        
        elif C_Mask.overlap(Block2_mask, (Block2x - x, Block2y - y)):
            if x + width > Block2x and x < Block2x + Block_width.get(Block2):
                if y > Block2y + 7:
                    y = Block2y + 50
                    jumpCount = -11
                if y - 20 < Block2y:
                    idle1 = True
                    y = Block2y - height

        elif C_Mask.overlap(Block3_mask, (Block3x - x, Block3y - y)):
            if x + width > Block3x and x < Block3x + Block_width.get(Block3):
                if y > Block3y + 7:
                    y = Block3y + 50
                    jumpCount = -11
                if y - 20 < Block3y:
                    y = Block3y - height
        
        elif C_Mask.overlap(Block4_mask, (Block4x - x, Block4y - y)):
            if x + width > Block4x and x < Block4x + Block_width.get(Block4):
                if y > Block4y + 7:
                    y = Block4y + 50
                    jumpCount = -11
                if y - 20 < Block4y:
                    y = Block4y - height

        elif C_Mask.overlap(Block5_mask, (Block5x - x, Block5y - y)):
            if x + width > Block5x and x < Block5x + Block_width.get(Block5):
                if y > Block5y + 7:
                    y = Block5y + 50
                    jumpCount = -11
                if y - 20 < Block5y:
                    y = Block5y - height
        
        elif C_Mask.overlap(Block6_mask, (Block6x - x, Block6y - y)):
            if x + width > Block6x and x < Block6x + Block_width.get(Block6):
                if y > Block6y + 7:
                    y = Block6y + 50
                    jumpCount = -11
                if y - 20 < Block6y:
                    y = Block6y - height

        elif C_Mask.overlap(Block7_mask, (Block7x - x, Block7y - y)):
            if x + width > Block7x and x < Block7x + Block_width.get(Block7):
                if y > Block7y + 7:
                    y = Block7y + 50
                    jumpCount = -11
                if y - 20 < Block7y:
                    idle1 = True
                    y = Block7y - height
        
        
        #Bullet shooting and position
        if Bullet_mask.overlap(Block1_mask, (Block1x - bx, Block1y - by)) or Bullet_mask.overlap(Block2_mask, (Block2x - bx, Block2y - by)) or Bullet_mask.overlap(Block3_mask, (Block3x - bx, Block3y - by)) or Bullet_mask.overlap(Block4_mask, (Block4x - bx, Block4y - by)) or Bullet_mask.overlap(Block5_mask, (Block5x - bx, Block5y - by)) or Bullet_mask.overlap(Block6_mask, (Block6x - bx, Block6y - by)) or Bullet_mask.overlap(Block7_mask, (Block7x - bx, Block7y - by)):
            shot = False
            bx = 1500

        if shot:
            bx += bvel
            if bx < -45:
                shot = False
            elif bx > 1500:
                shot = False
            if bx > 5 and LeftorRight:
                shot = True
            elif bx < 1500 and not LeftorRight:
                shot = True
        
        else:
            if keys[pygame.K_SPACE]:
                shot = True
                bx = x
                by = y + 25
                if LeftorRight:
                    Bullet = BulletLeft
                    bvel = -1 * abs(bvel)
                else:
                    Bullet = BulletRight
                    bvel = abs(bvel)

        #HpBar testing and practice    
        if keys[pygame.K_u]:
            if keys[pygame.K_LSHIFT]:
                hp_level = 100
        
        if hp_level <= 0:
            display.blit(GameOver, (600, 400))
            meterScore.append(score)
            Starting = True
            print(meterScore)
            
        #Camera angle
        #if y < 200:
        #   difference = 200 - y
        #  Block1y += difference
        # Block2y += difference
            #Block3y += difference
            

        #Meter/Score Counter 
        if not scroll:
            realy = 700 - y
        elif scroll:
            realy = 700 + (Floory - 760) + (700 - y)
        C_Meter = round(realy/100)
        Meters = font.render(f'Meters: {C_Meter}', True, (0, 0, 0))
        Blah = font.render(f"idle1 = {idle1}", True, (200,0,0))

        if pygame.mouse.get_pressed()[1] == True:
            Stuff = font.render(f"{Block1x, Block1y} \n{Block2x, Block2y} \n{Block3x, Block3y} \n{Block4x, Block4y} \n{Block5x, Block5y} \n{Block6x, Block6y} \n", True, (0,0,0))

        pygame.time.delay(sleeptime)
        display.blit(Bullet, (bx, by))
        #display.blit(C_Mask_Surface, (x, y))
        display.blit(Character, (x, y))
        display.blit(Block1, (Block1x, Block1y))
        display.blit(Block2, (Block2x, Block2y))
        display.blit(Block3, (Block3x, Block3y))
        display.blit(Block4, (Block4x, Block4y))
        display.blit(Block5, (Block5x, Block5y))
        display.blit(Block6, (Block6x, Block6y))
        display.blit(Block7, (Block7x, Block7y))
        display.blit(Stuff, (800, 500))
        display.blit(b1, (Block1x, Block1y))
        display.blit(b2, (Block2x, Block2y))
        display.blit(b3, (Block3x, Block3y))
        display.blit(b4, (Block4x, Block4y))
        display.blit(b5, (Block5x, Block5y))
        display.blit(b6, (Block6x, Block6y))
        display.blit(ENEMY1, (enemy1x, enemy1y))
        display.blit(Blah, (enemy1x, enemy1y - 30))
        display.blit(Floor, (1240, Floory))
        display.blit(Floor, (620, Floory))
        display.blit(Floor, (0, Floory))
        pygame.draw.rect(display, (0, 210, 0), (700, 25, hp_level, 30))
        pygame.draw.rect(display, (255, 255, 255), (700, 25, 100, 30), 3)
        pygame.draw.line(display, (255, 255, 255), (0, 200), (1500, 200))
        display.blit(HP_BAR, (625, 25))
        display.blit(Meters, (30, 25))
        pygame.display.update()