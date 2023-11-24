import pygame, sys
from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhisicsEntity, Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ninja Game')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320,240))


        self.clock = pygame.time.Clock()

        #self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        #self.img_pos = [160, 260]
        #self.img.set_colorkey((0, 0, 0))

        self.movement = [False, False]
        self.assets = {
            'decor':load_images('tiles/decor'),
            'grass':load_images('tiles/grass'),
            'stone':load_images('tiles/stone'),
            'large_decor':load_images('tiles/large_decor'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'player/run': Animation(load_images('entities/player/run'), img_dur=4),
            'player/jump': Animation(load_images('entities/player/jump')),
            'player/slide': Animation(load_images('entities/player/slide')),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
        }

        #self.collision_area = pygame.Rect(50, 50, 300, 50)

        self.clouds = Clouds(self.assets['clouds'], count=16)

        self.player = Player(self,(50,49), (8,15))

        self.tilemap = Tilemap(self, tile_size=16)

        self.scroll = [0, 0]

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 10
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 10
            
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            self.clouds.update()
            self.clouds.render(self.display, offset= render_scroll)

            self.tilemap.render(self.display, offset = render_scroll)
            self.player.update(self.tilemap, (self.movement[1]-self.movement[0],0))
            self.player.render(self.display, offset = render_scroll)


            #collision rectangle
            #img_r = pygame.Rect (self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            #if img_r.colliderect(self.collision_area):
            #    pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            #else:
            #    pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            #Cloud 
            #self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            #self.screen.blit(self.img, self.img_pos)

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
                        self.player. velocity[1] = -3
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_a:
                        self.movement[0] = False
                    if event.key == K_RIGHT or event.key == K_d:
                        self.movement[1] = False
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()