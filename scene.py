from os import path

import pygame
import pygame._sdl2 as sdl2

import settings

class Scene:
    def __init__(self, screenw, screenh, renderer, player_starting_posx):
        self.screenw, self.screenh = screenw, screenh
        self.renderer = renderer

        self.player_starting_posx = player_starting_posx

        self.load_texture()

    def load_texture(self):
        bg_image = pygame.image.load(path.join(settings.ASSETS_PATH, "background.png"))
        self.bg_texture = sdl2.Texture.from_surface(self.renderer, bg_image)
        self.bg_rect = self.bg_texture.get_rect()
        base_image = pygame.image.load(path.join(settings.ASSETS_PATH, "base.png"))
        self.base_texture = sdl2.Texture.from_surface(self.renderer, base_image)
        self.base_rect = self.base_texture.get_rect()

    def physics(self, dt, player_posx):
        self.offset_x = (player_posx - self.player_starting_posx) % self.base_rect.w

    def draw_base(self):
        for i in range(int(self.screenw / self.base_rect.w) + 2):
            self.renderer.blit(
                self.base_texture,
                pygame.Rect(
                    i * self.base_rect.w - self.offset_x,
                    self.screenh - self.base_rect.h,
                    *self.base_rect.size),
                self.base_rect
                )

    def draw_bg(self):
        self.renderer.blit(
            self.bg_texture,
            self.bg_rect,
            self.bg_rect
            )

