from os import path

import pygame
from pygame import mouse
import pygame._sdl2 as sdl2

import settings
from helpers import *


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
    TITLE_TEXT = "Game Over"
    TITLE_TEXT_SIZE = 40
    TITLE_TEXT_COLOUR = "Gray"
    TITLE_POSY = 200
    BUTTON_TEXT = "Restart"
    BUTTON_TEXT_SIZE = 30
    BUTTON_TEXT_COLOUR = "Green"
    BUTTON_POSY = 300
    BUTTON_NORMAL_COLOUR = (0, 255, 255, 255)
    BUTTON_HOVER_COLOUR = (0, 0, 255, 255)
    BUTTON_INFLATE_FACTOR = (10, 10)
    def __init__(self, screenw, screenh, renderer):
        self.screenw, self.screenh = screenw, screenh
        self.renderer = renderer

        self.title_tex, self.title_rect = text_to_texture(
            path.join(settings.ASSETS_PATH, "font_0.ttf"),
            self.TITLE_TEXT_SIZE,
            self.TITLE_TEXT,
            self.TITLE_TEXT_COLOUR,
            self.renderer,
            self.screenw / 2, self.TITLE_POSY
            )

        self.button_tex, self.button_rect = text_to_texture(
            path.join(settings.ASSETS_PATH, "font_0.ttf"),
            self.BUTTON_TEXT_SIZE,
            self.BUTTON_TEXT,
            self.BUTTON_TEXT_COLOUR,
            self.renderer,
            self.screenw / 2, self.BUTTON_POSY
            )
        self.button_bounding_rect =  self.button_rect.inflate(
            *self.BUTTON_INFLATE_FACTOR
            )
        self.button_bounding_rect.center = self.button_rect.center

        self.mouse_over_button = False

    def button_clicked(self, event):
        self.mouse_over_button = self.button_rect.collidepoint(
            pygame.mouse.get_pos()
            )
        if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_over_button:
            return True
        else:
            return False

    def physics(self):
        if self.mouse_over_button:
            self.button_colour = self.BUTTON_HOVER_COLOUR
        else:
            self.button_colour = self.BUTTON_NORMAL_COLOUR

    def draw(self):
        self.renderer.draw_color = self.button_colour
        self.renderer.draw_rect(
            self.button_bounding_rect,
            )
        self.renderer.blit(
            self.title_tex,
            self.title_rect,
            pygame.Rect(0, 0, *self.title_rect.size)
            )

        self.renderer.blit(
            self.button_tex,
            self.button_rect,
            pygame.Rect(0, 0, *self.button_rect.size)
            )

    def reset(self):
        self.mouse_over_button = False
