import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, MENU_OPTION, C_WHITE, C_BLUE_DARK


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/backgroundMenu.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('asset/musicMenu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)

            y_pos = 310

            for i in range(len(MENU_OPTION)):
                text_size = 40
                spacing = 60

                if MENU_OPTION[i] == "Novo Jogo":
                    text_size = 60
                    spacing = 70

                if MENU_OPTION[i] == "SCORE" or MENU_OPTION[i] == "SAIR":
                    text_size = 30
                    spacing = 50

                if i == menu_option:
                    self.menu_text(text_size, MENU_OPTION[i], C_BLUE_DARK, ((WIN_WIDTH / 2), y_pos), True)
                else:
                    self.menu_text(text_size, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), y_pos))

                y_pos += spacing

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, selected: bool = False):
        text_font: Font = pygame.font.SysFont(name="georgia", size=text_size)

        if selected:
            outline_size = 1

            outline_surf: Surface = text_font.render(text, True, C_WHITE).convert_alpha()

            for dx in range(-outline_size, outline_size + 1):
                for dy in range(-outline_size, outline_size + 1):
                    if dx != 0 or dy != 0:
                        outline_rect: Rect = outline_surf.get_rect(
                            center=(text_center_pos[0] + dx, text_center_pos[1] + dy)
                        )
                        self.window.blit(source=outline_surf, dest=outline_rect)

        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
