import pygame


class Enemy(pygame.sprite.Sprite):
    """Class Enemy"""

    def __init__(self, screen):
        """ """
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("Images/Enemy/Enemy_01.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Draw Enemy"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move Enemy"""
        self.y += 0.5
        self.rect.y = self.y


if __name__ == "__main__":
    pass
