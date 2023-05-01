import pygame

from Gun.Gun import Gun
from typing import Tuple


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, gun: Gun):
        """Create Bullet"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.gun = gun

        self.rect = pygame.Rect(0, 3, 2, 6)
        self.color = (53, 181, 89)
        self.speed = 5.0
        self.rect.centerx = self.gun.rect.centerx
        self.rect.top = self.gun.rect.top
        self.y = float(self.gun.rect.top)

    def update(self):
        """Move Bullet for Y"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw Bullet in The Window"""
        pygame.draw.rect(self.screen, self.color, self.rect)
