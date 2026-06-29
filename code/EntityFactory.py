#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Background import Background
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case name if name.startswith('Level') and name.endswith('Bg'):
                list_bg = []

                for i in range(3):
                    list_bg.append(Background(f'{name}{i}', (0, 0)))
                    list_bg.append(Background(f'{name}{i}', (WIN_WIDTH, 0)))

                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))
            case name if name.startswith('Enemy'):
                return Enemy(name, (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
