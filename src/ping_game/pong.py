import sys
import pygame
import random
# todo: bug att man kan röra sig utanför screen.
class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((1280, 720))
        
        self.clock = pygame.time.Clock()
        self.x, self.y = self.screen.get_size()

        self.player_shape = [20, 85]
        
        self.p1_pos = [5, self.y/2-45]
        self.p1_movement = [False, False]

        self.p2_pos = [self.x-20-5, self.y/2-45]
        self.p2_movement = [False, False]

        self.ball_y_axis = random.randrange(-5, 5)
        # self.ball_x_axis = 
        self.ball_pos = [self.x/2, self.y/2]
        self.ball_speed = -5

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            # p1 up
            if self.p1_pos[1] >= 0:
                self.p1_pos[1] += self.p1_movement[1] - self.p1_movement[0] * 9
            # p2 down
            if self.p1_pos[1] <= 635:
                self.p1_pos[1] -= self.p1_movement[0] - self.p1_movement[1] * 9
            # p2 up
            if self.p2_pos[1] >= 0:
                self.p2_pos[1] += self.p2_movement[1] - self.p2_movement[0] * 9
            # p2 down
            if self.p2_pos[1] <= 635:
                self.p2_pos[1] -= self.p2_movement[0] - self.p2_movement[1] * 9

            self.ball_pos = [self.ball_pos[0] + self.ball_speed, self.ball_pos[1] + self.ball_y_axis]

            self.p1 = pygame.draw.rect(self.screen, "white", (*self.p1_pos, *self.player_shape))
            self.p2 = pygame.draw.rect(self.screen, "white", (*self.p2_pos, *self.player_shape))
            self.ball = pygame.draw.circle(self.screen, "white", (self.ball_pos), 15)
            # ball bounces on p1
            if self.ball.colliderect(self.p1):
                self.ball_speed = -self.ball_speed*1.1
                if self.p1_movement[1] and self.ball_y_axis <= 8:
                    self.ball_y_axis += 1.5
                if self.p1_movement[0] and self.ball_y_axis >= -8:
                    self.ball_y_axis -= 1.5
            # ball bounces on p2
            if self.ball.colliderect(self.p2):
                self.ball_speed = -self.ball_speed*1.1
                if self.p2_movement[1] and self.ball_y_axis <= 8:
                    self.ball_y_axis += 1.5
                if self.p2_movement[0] and self.ball_y_axis >= -8:
                    self.ball_y_axis -= 1.5
            # ball bounces on roof
            if 15 > self.ball_pos[1]:
                self.ball_y_axis = -self.ball_y_axis
            # ball bounces on floor
            if self.y-15 < self.ball_pos[1]:
                self.ball_y_axis = -self.ball_y_axis

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    print("p1-y:", self.p1.y)
                    print("p2-y:", self.p2.y)
                    print("ball-x:", self.ball.x, "ball-y:", self.ball.y)
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_w:
                        self.p1_movement[0] = True
                    if e.key == pygame.K_s:
                        self.p1_movement[1] = True
                    if e.key == pygame.K_UP:
                        self.p2_movement[0] = True
                    if e.key == pygame.K_DOWN:
                        self.p2_movement[1] = True
                if e.type == pygame.KEYUP:
                    if e.key == pygame.K_w:
                        self.p1_movement[0] = False
                    if e.key == pygame.K_s:
                        self.p1_movement[1] = False
                    if e.key == pygame.K_UP:
                        self.p2_movement[0] = False
                    if e.key == pygame.K_DOWN:
                        self.p2_movement[1] = False
                
            pygame.display.update()
            self.clock.tick(60)

Game().run()