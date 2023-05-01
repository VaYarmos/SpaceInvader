import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen: pygame.Surface):
        """Initialization Gun"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("Images/Gun/Gun.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom - 10

        self.move_right = False
        self.move_left = False

    def output(self):
        """Draw Gun"""
        self.screen.blit(self.image, self.rect)

    def update_gun_position(self):
        """Update Gun Position"""
        if self.move_right and self.rect.right < self.screen_rect.right - 10:
            self.center += 1.5

        if self.move_left and self.rect.left > self.screen_rect.left + 10:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        """ Set Gun In Start """
        self.center = self.screen_rect.centerx


if __name__ == "__main__":
    pass
