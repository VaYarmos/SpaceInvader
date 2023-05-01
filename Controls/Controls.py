import json

import pygame
import sys
import time
from typing import Tuple

from pygame.sprite import Group
from Gun.Gun import Gun
from Bullet.Bullet import Bullet
from Enemy.Enemy import Enemy
from Stats.Stats import Stats
from Score.Score import Score


class Controls:
    def __init__(
            self,
            screen: pygame.Surface,
            gun: Gun,
            bullets: Group,
            enemy: Group,
            stats: Stats,
            score: Score,
    ):
        self.screen = screen
        self.gun = gun
        self.bullets = bullets
        self.enemy = enemy
        self.stats = stats
        self.score = score

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Shot
                if event.key == pygame.K_SPACE:
                    new_bullet = Bullet(self.screen, self.gun)
                    self.bullets.add(new_bullet)
                # Move Gun Right
                if event.key == pygame.K_d:
                    self.gun.move_right = True

                # Move Gun Left
                elif event.key == pygame.K_a:
                    self.gun.move_left = True

            elif event.type == pygame.KEYUP:
                # Shot
                if event.key == pygame.K_SPACE:
                    self.gun.shot = False

                # Stop Move Gun Right
                if event.key == pygame.K_d:
                    self.gun.move_right = False

                # Stop Move Gun Left
                if event.key == pygame.K_a:
                    self.gun.move_left = False

    def update_screen(self, bg_color: Tuple):
        self.screen.fill(bg_color)
        self.score.show_score()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.gun.output()
        self.enemy.draw(self.screen)
        pygame.display.flip()

    def update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(self.bullets, self.enemy, True, True)
        if collisions:
            for enemy in collisions.values():
                self.stats.score += 10 * len(enemy)
            self.score.draw_image()
            self.check_high_score()
            self.score.image_heals()
        if len(self.enemy) == 0:
            self.bullets.empty()
            self.create_enemy()

    def create_enemy(self):
        """Create Army Enemy"""
        enemy = Enemy(self.screen)
        enemy_width = enemy.rect.width
        enemy_height = enemy.rect.height
        number_enemy_x = int((1200 - 2 * enemy_width) / enemy_width)
        number_enemy_y = int((800 - 100 - 2 * enemy_height) / enemy_height)

        for row in range(number_enemy_y):
            for column in range(number_enemy_x):
                enemy = Enemy(self.screen)
                enemy.x = enemy_width + enemy_width * column
                enemy.y = enemy_height + enemy_height * row
                enemy.rect.x = enemy.x
                enemy.rect.y = enemy.rect.height + (enemy.rect.height * row)
                self.enemy.add(enemy)

    def update_enemy(self):
        """Update Enemy"""
        self.enemy.update()
        if pygame.sprite.spritecollideany(self.gun, self.enemy):
            self.gun_kill()
        self.enemy_check()

    def gun_kill(self):
        """"""
        if self.stats.guns_left > 0:
            self.stats.guns_left -= 1
            self.score.image_heals()
            self.enemy.empty()
            self.bullets.empty()
            self.create_enemy()
            self.gun.create_gun()
            time.sleep(1)
        else:
            self.stats.run_game = False
            sys.exit()

    def enemy_check(self):
        """ Check If Enemy Move To Base """
        screen_rect = self.screen.get_rect()
        for enemy in self.enemy:
            if enemy.rect.bottom >= screen_rect.bottom:
                self.gun_kill()
                break

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.score.image_high_score()
            with open('Score/high_score.json', 'w') as file:
                json.dump({
                    "High Score": self.stats.score
                }, file)


if __name__ == "__main__":
    pass
