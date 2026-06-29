import pygame

# C
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_BLUE_DARK = (2, 0, 101)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 5,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 5,
    'Level3Bg0': 0,
    'Level3Bg1': 1,
    'Level3Bg2': 5,
    'Level4Bg0': 0,
    'Level4Bg1': 1,
    'Level4Bg2': 5,

    'Player1': 5,
    'Player1Shot': 8,
    'Player2': 5,
    'Player2Shot': 8,

    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 4,
    'Enemy3': 2,
    'Enemy3Shot': 5,
    'Enemy4': 2,
    'Enemy4Shot': 6,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level4Bg0': 999,
    'Level4Bg1': 999,
    'Level4Bg2': 999,

    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,

    'Enemy1': 25,
    'Enemy1Shot': 1,
    'Enemy2': 35,
    'Enemy2Shot': 1,
    'Enemy3': 45,
    'Enemy3Shot': 1,
    'Enemy4': 55,
    'Enemy4Shot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level4Bg0': 0,
    'Level4Bg1': 0,
    'Level4Bg2': 0,

    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,

    'Enemy1': 1,
    'Enemy1Shot': 10,
    'Enemy2': 1,
    'Enemy2Shot': 12,
    'Enemy3': 1,
    'Enemy3Shot': 15,
    'Enemy4': 1,
    'Enemy4Shot': 18,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level4Bg0': 0,
    'Level4Bg1': 0,
    'Level4Bg2': 0,

    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,

    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Enemy3': 150,
    'Enemy3Shot': 0,
    'Enemy4': 200,
    'Enemy4Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 18,
    'Player2': 18,
    'Enemy1': 140,
    'Enemy2': 120,
    'Enemy3': 100,
    'Enemy4': 80,
}

# L
LEVELS = ('Level1', 'Level2', 'Level3', 'Level4')

# M
MENU_OPTION = ('Novo Jogo',
               'Novo Jogo - 2 Jogadores - Cooperativo',
               'Novo Jogo - 2 Jogadores - Competitivo',
               'SCORE',
               'SAIR')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 1000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 3000

# W
WIN_WIDTH = 800
WIN_HEIGHT = 600

# S

SCORE_POS = {
    'Top10': (WIN_WIDTH / 2, 100),
    'Title': (WIN_WIDTH / 2, 130),
    'SubTitle': (WIN_WIDTH / 2, 200),
    'EnterName': (WIN_WIDTH / 2, 350),
    'Label': (WIN_WIDTH / 2 - 80, 150),
    'Name': (WIN_WIDTH / 2, 350)
}
