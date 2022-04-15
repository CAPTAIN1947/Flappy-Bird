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
        font_name,
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