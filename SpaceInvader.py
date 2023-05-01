import json

import pygame
from pygame.sprite import Group

from Controls.Controls import Controls
from Gun.Gun import Gun
from Enemy.Enemy import Enemy
from Stats.Stats import Stats
from Score.Score import Score


class SpaceInvader:
    def __init__(self, width: int = 1200, height: int = 1200):
        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Space Invader")
        self.bg_color = (0, 0, 0)
        self.windows_clock = pygame.time.Clock()

        self.gun = Gun(self.screen)
        self.bullets = Group()
        self.enemy = Group()
        self.stats = Stats()
        self.score = Score(self.screen, self.stats)

        # Create Controls Events
        self.controls = Controls(
            self.screen, self.gun, self.bullets, self.enemy, self.stats, self.score
        )
        self.controls.create_enemy()

        self.__start()

    def __start(self):
        while True:
            self.controls.events()
            if self.stats.run_game:
                self.gun.update_gun_position()
                self.controls.update_screen(self.bg_color)
                self.controls.update_bullet()
                self.controls.update_enemy()
            else:
                pass


if __name__ == "__main__":
    SpaceInvader()
