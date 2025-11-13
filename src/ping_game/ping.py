import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ping")
x, y = screen.get_size()
print(x, y)
pygame.draw.rect(screen, (255,255,255),[5,y/2-50,20,100])
pygame.draw.rect(screen, (255,255,255), [x-25,y/2-50, 20,100])
pygame.draw.circle(screen, (255,255,255), (x/2, y/2), 20)
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()