import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_WHITE, SCORE_POS, MENU_OPTION, WIN_WIDTH
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('asset/Score.mp3')
        pygame.mixer_music.play(-1)

        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.score_text(90, 'VOCÊ GANHOU!!', C_WHITE, SCORE_POS['Title'])
            self.score_text(60, 'PARABÉNS!', C_WHITE, SCORE_POS['SubTitle'])

            text = 'DIGITE SEU NOME PARA SALVAR O SCORE'
            score = player_score[0]
            winner_text = ''

            if game_mode == MENU_OPTION[0]:
                score = player_score[0]

            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'DIGITE O NOME DO TIME PARA SALVAR O SCORE'

            if game_mode == MENU_OPTION[2]:
                if player_score[0] > player_score[1]:
                    score = player_score[0]
                    winner_text = 'JOGADOR 1 VENCEU!'
                    text = 'QUAL O NOME DO PLAYER 1?'
                elif player_score[1] > player_score[0]:
                    score = player_score[1]
                    winner_text = 'JOGADOR 2 VENCEU!'
                    text = 'QUAL O NOME DO PLAYER 2?'
                else:
                    score = player_score[0]
                    winner_text = 'EMPATE!'
                    text = 'DIGITE UM NOME PARA REGISTRAR'

            if winner_text:
                self.score_text(38, winner_text, C_WHITE, (WIN_WIDTH / 2, 245))

            self.score_text(46, f'PONTUAÇÃO FINAL: {int(score):05d}', C_WHITE, (WIN_WIDTH / 2, 295))
            self.score_text(32, text, C_WHITE, (WIN_WIDTH / 2, 340))
            self.score_text(28, 'PRESSIONE ENTER PARA CONFIRMAR', C_WHITE, (WIN_WIDTH / 2, 440))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and 1 <= len(name) <= 12:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        db_proxy.close()
                        self.show()
                        return

                    elif event.key == K_BACKSPACE:
                        name = name[:-1]

                    else:
                        if len(name) < 12 and event.unicode.isprintable():
                            name += event.unicode.upper()

            display_name = name if name else '_'
            self.score_text(52, display_name, C_WHITE, (WIN_WIDTH / 2, 390))
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('asset/Score.mp3')
        pygame.mixer_music.play(-1)

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.score_text(68, 'TOP 10 SCORE', C_WHITE, SCORE_POS['Top10'])

            self.score_text(38, 'NOME', C_WHITE, (220, 160))
            self.score_text(38, 'SCORE', C_WHITE, (400, 160))
            self.score_text(38, 'DATA', C_WHITE, (590, 160))

            for index, player_score in enumerate(list_score):
                id_, name, score, date = player_score
                y_pos = 200 + (index * 30)

                self.score_text(30, name[:12], C_WHITE, (220, y_pos))
                self.score_text(30, f'{int(score):05d}', C_WHITE, (400, y_pos))
                self.score_text(30, date, C_WHITE, (590, y_pos))

            self.score_text(24, 'PRESSIONE (ESC) PARA VOLTAR', C_WHITE, (WIN_WIDTH / 2, 560))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"