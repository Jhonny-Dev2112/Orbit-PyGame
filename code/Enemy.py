#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1

        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]

            shot_sound = pygame.mixer.Sound('./asset/ShotEnemies.mp3')
            shot_sound.set_volume(0.2)
            shot_sound.play()

            return EnemyShot(
                name=f'{self.name}Shot',
                position=(self.rect.centerx - 80, self.rect.centery - 4)
            )