import pygame, sys
pygame.init()

display = pygame.display.set_mode((1000, 1000))
x = 40
y = 40
points = []

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()
    display.fill((255, 255, 255))
    x = 40
    y = 40
    points = []
    for i in range(24):
        for i in range (24):
            pygame.draw.circle(display, (0,0,0), (x, y), 5)
            x += 40
            pos = pygame.mouse.get_pos()
            points.append((x, y))
            if pygame.mouse.get_pressed()[0]:
                print(points)
        x = 40
        y += 40
    pygame.draw.rect(display, (0,0,0), (0, 0, 1000, 1000), 10)
    pygame.display.update()