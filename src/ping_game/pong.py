import sys
import pygame

class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_caption("rogueLike")
        self.screen = pygame.display.set_mode((1280, 720))
        
        self.clock = pygame.time.Clock()
        self.x, self.y = self.screen.get_size()

        self.player_shape = [20, 85]
        # self.player_collision = pygame.Rect
        self.p1_pos = [5, self.y/2-45]
        self.p1_movement = [False, False]

        self.p2_pos = [self.x-20-5, self.y/2-45]
        self.p2_movement = [False, False]
        self.ball_pos = [self.x/2, self.y/2]
        
    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            # p1 up
            self.p1_pos[1] += self.p1_movement[1] - self.p1_movement[0] * 9
            # p2 down
            self.p1_pos[1] -= self.p1_movement[0] - self.p1_movement[1] * 9
            # p1 up
            self.p2_pos[1] += self.p2_movement[1] - self.p2_movement[0] * 9
            # p2 down
            self.p2_pos[1] -= self.p2_movement[0] - self.p2_movement[1] * 9
            pygame.draw.rect(self.screen, "white", (*self.p1_pos, *self.player_shape))
            pygame.draw.rect(self.screen, "white", (*self.p2_pos, *self.player_shape))
            pygame.draw.circle(self.screen, "white", (self.ball_pos), 15)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
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