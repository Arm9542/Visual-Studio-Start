import pygame, sys, random, math
pygame.init()

'''else:
            #self.y += 1.25
            self.mouse = pygame.mouse.get_pressed()[0]
            if self.mouse:
                self.jump = True'''

display = pygame.display.set_mode((750, 750))
class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.jump = False
        self.jumpCount = 10
        self.keys = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()[0]
        self.bird = pygame.image.load("FlappyBird.png")
    def Jump(self):
        self.mouse = pygame.mouse.get_pressed()[0]
        if self.jump == True:
            if self.jumpCount > 0:
                self.y -= self.jumpCount**2 * 0.08
                self.jumpCount -= 1
            else:
                self.jump = False
                self.jumpCount = 10
        else:
            self.y += 1.25
            if self.mouse:
                self.jump = True
    
    def Draw(self):   
        display.blit(self.bird, (self.x, self.y))
    
    def Collision(self, rect):
        bird_rect = pygame.rect.Rect(self.x, self.y, 32, 22)
        if bird_rect.colliderect(rect):
            return True
        return False
x = 100
y = 375
jump = False
jumpCount = 10
bottomy = random.randint(75, 675)
bottom2y = random.randint(75, 675)
topy = bottomy - 900
top2y = bottom2y - 900
player_rect = pygame.rect.Rect(x, y, 30, 30)
pipex = 350
pipe2x = 700
top_pipe = pygame.rect.Rect(pipex, topy, 65, 680)
bottom_pipe = pygame.rect.Rect(pipex, bottomy, 65, 680)
top_pipe2 = pygame.rect.Rect(pipe2x, top2y, 65, 680) 
bottom_pipe2 = pygame.rect.Rect(pipe2x, bottom2y, 65, 680)
bird = Player(100, 375)
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
    display.fill((74, 174, 240))
    if pipex < 0:
        pipex = 700
        bottomy = random.randint(150, 675)
        topy = bottomy - 900
    else:
        pipex -= 0.6
    if pipe2x < 0:
        pipe2x = 700
        bottom2y = random.randint(150, 675)
        top2y = bottom2y - 900
    else:
        pipe2x -= 0.6
    bird.Jump()
    if bird.Collision(top_pipe) or bird.Collision(bottom_pipe) or bird.Collision(top_pipe2) or bird.Collision(bottom_pipe2) or bird.y < 0 or bird.y > 780:
        pygame.time.delay(500)
        break
    bird.Draw()
    pygame.draw.rect(display, (10, 194, 4), top_pipe)
    pygame.draw.rect(display, (10, 194, 4), bottom_pipe)
    pygame.draw.rect(display, (10, 194, 4), top_pipe2)
    pygame.draw.rect(display, (10, 194, 4), bottom_pipe2)
    pygame.time.delay(3)
    player_rect = pygame.rect.Rect(x, y, 30, 30)
    top_pipe = pygame.rect.Rect(pipex, topy, 65, 680)
    bottom_pipe = pygame.rect.Rect(pipex, bottomy, 65, 680)
    top_pipe2 = pygame.rect.Rect(pipe2x, top2y, 65, 680)
    bottom_pipe2 = pygame.rect.Rect(pipe2x, bottom2y, 65, 680)
    #pygame.draw.circle(display, (240, 240, 0), (x, y), 15)
    pygame.display.update()