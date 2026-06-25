# C
import pygame

COLOR_WHITE = (255,255,255)
COLOR_YELLOW = (255,255,0)
COLOR_BLUE_DARK = (2, 0, 101)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 5,
    'Player1' : 5,
    'Player1Shot': 5,
    'Player2' : 5,
    'Player2Shot': 5,
    'Enemy1': 2,
    'Enemy1Shot': 4,
    'Enemy2': 1,
    'Enemy2Shot': 3,
    'Enemy3': 4,
    'Enemy4': 4,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 5,
    'Enemy2': 70,
    'Enemy2Shot': 2
}

ENTITY_SHOT_DELAY = {
    'Player1' : 20,
    'Player2' : 20,
    'Enemy1' : 100,
    'Enemy2' : 250,
}

# M
MENU_OPTION = ('New Game',
               'New Game 2P - COOPERATIVE',
               'New Game 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

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
SPAWN_TIME = 4000

# W
WIN_WIDTH = 800
WIN_HEIGHT = 600

