from os import path

import pygame
import pygame._sdl2 as sdl2

import settings


class HUD:
    def __init__(self, screenw, screenh, renderer):
        self.screenw, self.screenh = screenw, screenh
        self.renderer = renderer

        self.score = Score(self.screenw, self.screenh, self.renderer)

    def physics(self, player_score):
        self.score.physics(player_score)

    def draw(self):
        self.score.draw()


class Score:
    TEXT_SIZE = 40
    TEXT_COLOUR = "Red"
    TEXT_SPACING = 30
    POSY = 30
    def __init__(self, screenw, screenh, renderer):
        self.screenw, self.screenh = screenw, screenh
        self.renderer = renderer

        char_sheet_img = pygame.image.load(path.join(settings.ASSETS_PATH, "text.png"))
        char_sheet_img.set_colorkey((255, 255, 255, 255))
        self.char_sheet = sdl2.Texture.from_surface(
            self.renderer,
            char_sheet_img
            )
        self.rows = 10
        self.char_rect = pygame.Rect(
            0,
            0,
            self.char_sheet.width / 10,
            self.char_sheet.height
        )

    def physics(self, player_score):
        self.score_list = [int(i) for i in str(player_score)]

    def draw(self):
        for i in range(len(self.score_list)):
            self.renderer.blit(
                self.char_sheet,
                pygame.Rect(
                    self.get_center_posx(i), self.POSY,
                    *self.char_rect.size
                    ),
                pygame.Rect(
                    self.score_list[i] * self.char_rect.w, 0,
                    *self.char_rect.size
                    )
                )

    def get_center_posx(self, i):
        width = self.TEXT_SPACING * (len(self.score_list) - 1) + self.char_rect.w
        return (self.screenw / 2 - width / 2) + (i * self.TEXT_SPACING)
