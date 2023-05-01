import pygame.font
from Gun.Gun import Gun
from pygame.sprite import Group


class Score:
    """ Output Score """

    def __init__(self, screen, stats):
        """ """
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()
        self.text_color = (53, 181, 89)
        self.font = pygame.font.SysFont(None, 64)
        self.draw_image()
        self.image_high_score()
        self.image_heals()

    def draw_image(self):
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        self.high_score = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_heals(self):
        """

        :return:
        """
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            gun.s
            self.guns.add(gun)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score, self.high_score_rect)
        self.guns.draw(self.screen)


if __name__ == '__main__':
    pass
