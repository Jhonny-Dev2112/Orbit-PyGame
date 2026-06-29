#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, LEVELS
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def show_game_over(self):
        game_over_bg = pygame.image.load('./asset/GameOverBg.png').convert()
        game_over_bg = pygame.transform.scale(game_over_bg, (WIN_WIDTH, WIN_HEIGHT))

        pygame.mixer_music.stop()
        pygame.mixer_music.load('./asset/GameOver.mp3')
        pygame.mixer_music.play()

        start_time = pygame.time.get_ticks()

        while pygame.time.get_ticks() - start_time < 3000:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.window.blit(game_over_bg, (0, 0))
            pygame.display.flip()

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Player1, Player2]
                player_health = [300, 300]  # [Player1, Player2]
                game_finished = True

                for level_name in LEVELS:
                    level = Level(self.window, level_name, menu_return, player_score, player_health)
                    level_return = level.run(player_score, player_health)

                    if not level_return:
                        game_finished = False
                        break

                if game_finished:
                    score.save(menu_return, player_score)
                else:
                    self.show_game_over()

            elif menu_return == MENU_OPTION[3]:
                score.show()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()