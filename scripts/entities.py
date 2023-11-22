import pygame

class PhisicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.colllisions = {'up': False, 'down': False, 'right': False, 'left': False}

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0, 0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.colllisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right=rect.left
                    self.colllisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left=rect.right
                    self.colllisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom=rect.top
                    self.colllisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top=rect.bottom
                    self.colllisions['up'] = True
                self.pos[1] = entity_rect.y

        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        if self.colllisions['down'] or self.colllisions['up']:
            self.velocity[1]=0

    def render(self, surf, offset = (0, 0)):
        surf.blit(self.game.assets["player"], (self.pos[0] - offset[0], self.pos[1] - offset[1]))
