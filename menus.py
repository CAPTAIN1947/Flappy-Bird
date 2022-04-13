from os import path

import pygame
import pygame._sdl2 as sdl2

import settings


def text_to_texture(
    font_name,
    font_size,
    text,
    text_colour,
    renderer,
    posx, posy,
    ):
    font = pygame.font.Font(
        path.join(settings.ASSETS_PATH, "font_0.ttf"),
        font_size
        )
    text = font.render(
        text,
        False,
        text_colour
        )
    texture = sdl2.Texture.from_surface(renderer, text)
    texture_rect = texture.get_rect(center = (posx, posy))
    return texture, texture_rect


class MainMenu:
    TITLE_TEXT_SIZE = 40
    TITLE_TEXT_COLOUR = "Red"
    TITLE_POSY = 60
    INSTRUCTION_TEXT = "TAP or CLICK to Play"
    INSTRUCTION_TEXT_SIZE = 20
    INSTRUCTION_TEXT_COLOUR = "Green"
    INSTRUCTION_POSY = 300
    def __init__(self, screenw, screenh, renderer):
        self.screenw, self.screenh = screenw, screenh
        self.renderer = renderer

        self.title_tex, self.title_rect = text_to_texture(
            path.join(settings.ASSETS_PATH, "font_0.ttf"),
            self.TITLE_TEXT_SIZE,
            settings.TITLE,
            self.TITLE_TEXT_COLOUR,
            self.renderer,
            self.screenw / 2, self.TITLE_POSY
            )

        self.intruction_tex, self.intruction_rect = text_to_texture(
            path.join(settings.ASSETS_PATH, "font_0.ttf"),
            self.INSTRUCTION_TEXT_SIZE,
            self.INSTRUCTION_TEXT,
            self.INSTRUCTION_TEXT_COLOUR,
            self.renderer,
            self.screenw / 2, self.INSTRUCTION_POSY
            )

    def draw(self):
        self.renderer.blit(
            self.title_tex,
            self.title_rect,
            pygame.Rect(0, 0, *self.title_rect.size)
            )

        self.renderer.blit(
            self.intruction_tex,
            self.intruction_rect,
            pygame.Rect(0, 0, *self.intruction_rect.size)
            )


class GameOverMenu:
    def __init__(self):
        pass
