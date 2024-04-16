import pygame, sys, random, math
pygame.init()

display = pygame.display.set_mode((750, 750))
x = 100
y = 375
jump = False
jumpCount = 10
bottomy = random.randint(270, 675)
bottom2y = random.randint(270, 675)
topy = bottomy - 900
top2y = bottom2y - 900
player_rect = pygame.rect.Rect(x, y, 30, 30)
pipex = 350
pipe2x = 700
top_pipe = pygame.rect.Rect(pipex, topy, 65, 680)
bottom_pipe = pygame.rect.Rect(pipex, bottomy, 65, 680)
top_pipe2 = pygame.rect.Rect(pipe2x, top2y, 65, 680) 
bottom_pipe2 = pygame.rect.Rect(pipe2x, bottom2y, 65, 680)
class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.jump = False
        self.jumpCount = 10
        self.keys = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()[0]
        self.player = pygame.image.load("FlappyBird.png")
    def Jump_AI(self, jump):
        if jump:
            if self.jumpCount > 0:
                self.y -= self.jumpCount**2 * 0.08
                self.jumpCount -= 1
            else:
                self.jump = False
                self.jumpCount = 10
        else:
            self.y += 1.25
    
    def Draw(self):   
        display.blit(self.player, (self.x, self.y))
    
    def Collision(self, rect):
        player_rect = pygame.rect.Rect(self.x, self.y, 32, 22)
        if player_rect.colliderect(rect):
            return True
        return False
player = Player(75, 375)
score = 0
font = pygame.font.SysFont("Comic Sans MS", 32)
Scoreboard = font.render(f"Score: {score}", True, (0,0,0))
bias = 0
top_y_weight = 0
bottom_y_weight = 0
pipe_x = 0
pipe_x_weight = 0
sum = 0
gen = 1
Birds = [player]
for i in range(5):
    birdie = Player(75, 375)
    Birds.append(birdie)
print(len(Birds))
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
    Birds[1].Jump_AI(keys[pygame.K_w])
    Birds[1].Draw()
    Birds[3].Jump_AI(keys[pygame.K_1])
    Birds[3].Draw()
    if pipex < 0:#Moving the pipes towards the bird and resetting them
        pipex = 700
        bottomy = random.randint(270, 675)
        topy = bottomy - 900
        score += 1
    else:
        pipex -= 0.6
    if pipe2x < 0:
        pipe2x = 700
        bottom2y = random.randint(270, 675)
        top2y = bottom2y - 900
        score +=1
    else:
        pipe2x -= 0.6
    if pipex - player.x < pipe2x - player.x and pipex > 75:#Calculates the distance from the bird to the pipe
        pipe_x = pipex - player.x
    elif pipe2x - player.x < pipex - player.x and pipe2x > 75:
        pipe_x = pipe2x - player.x
    player.Jump_AI(pygame.mouse.get_pressed()[0])
    if player.Collision(top_pipe) or player.Collision(bottom_pipe) or player.Collision(top_pipe2) or player.Collision(bottom_pipe2) or player.y < 0 or player.y > 780:
        pygame.time.delay(500)
        break
    player.Draw()
    if keys[pygame.K_y]:
        pygame.time.delay(1000)
    pygame.draw.rect(display, (10, 194, 4), top_pipe)
    pygame.draw.rect(display, (10, 194, 4), bottom_pipe)
    pygame.draw.rect(display, (10, 194, 4), top_pipe2)
    pygame.draw.rect(display, (10, 194, 4), bottom_pipe2)
    Scoreboard = font.render(f"Score: {score}", True, (0,0,0))
    display.blit(Scoreboard, (10, 20))
    pygame.time.delay(3)
    player_rect = pygame.rect.Rect(x, y, 30, 30)
    top_pipe = pygame.rect.Rect(pipex, topy, 65, 680)
    bottom_pipe = pygame.rect.Rect(pipex, bottomy, 65, 680)
    top_pipe2 = pygame.rect.Rect(pipe2x, top2y, 65, 680)
    bottom_pipe2 = pygame.rect.Rect(pipe2x, bottom2y, 65, 680)
    #pygame.draw.circle(display, (240, 240, 0), (x, y), 15)
    pygame.display.update()