import pygame, sys
from scripts.utils import load_images
from scripts.tilemap import Tilemap
from pygame.locals import *

RENDER_SCALE = 2.0

class Editor:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Editor')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320,240))

        self.clock = pygame.time.Clock()

        self.assets = {
            'decor':load_images('tiles/decor'),
            'grass':load_images('tiles/grass'),
            'stone':load_images('tiles/stone'),
            'large_decor':load_images('tiles/large_decor'),
        }

        self.movement = [False, False, False, False]

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0]

    def run(self):
        while True:
            self.display.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_LEFT or event.key == K_a:
                        self.movement[0] = True
                    if event.key == K_RIGHT or event.key == K_d:
                        self.movement[1] = True
                    if event.key == K_UP or event.key == K_w:
                        self.movement[2] = True
                    if event.key == K_DOWN or event.key == K_s:
                        self.movement[3] = True
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_a:
                        self.movement[0] = False
                    if event.key == K_RIGHT or event.key == K_d:
                        self.movement[1] = False
                    if event.key == K_UP or event.key == K_w:
                        self.movement[2] = False
                    if event.key == K_DOWN or event.key == K_s:
                        self.movement[3] = False
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Editor().run()