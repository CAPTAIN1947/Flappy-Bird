from os import path

import random

import pygame
import pygame._sdl2 as sdl2

import settings


class Pipe:
    GAP = 100 # Gap between the upper and the lower part
    WIDTH = 64
    def __init__(self, _id, pos, tex_rect):
        self._id = _id
        self.pos = pos
        self.tex_rect = tex_rect

        self.gap_rect = pygame.Rect(0, 0, self.WIDTH, self.GAP)
        self.gap_rect.midleft = self.pos

        self.lower_rect = pygame.Rect(self.tex_rect)
        self.upper_rect = pygame.Rect(self.tex_rect)
        self.lower_rect.topleft = self.gap_rect.bottomleft
        self.upper_rect.bottomleft = self.gap_rect.topleft

        self.crossed_player = False

    def __str__(self):
        return "pos: {}, {}".format(self.pos.x, self.pos.y)

    def physics(self, dt, player_velx, player_state):
        if player_state not in ("collided", "died"):
            self.pos.x -= player_velx * dt
        self.lower_rect.left = self.upper_rect.left = self.gap_rect.left = self.pos.x

    def draw(self, renderer, tex_up, tex_down):
        renderer.blit(
            tex_up,
            self.upper_rect,
            self.tex_rect
            )
        renderer.blit(
            tex_down,
            self.lower_rect,
            self.tex_rect
            )
        renderer.draw_color = (255, 0, 0, 255)
        renderer.draw_rect(
            self.upper_rect
            )

    def collide_with_player(self, player_rect):
        return self.upper_rect.colliderect(player_rect) or self.lower_rect.colliderect(player_rect)

    def is_out_of_screen(self):
        if self.gap_rect.right < 0:
            return True
        else:
            return False

    def check_if_crossed_player(self, player_posx):
        if not self.crossed_player and self.pos.x < player_posx:
            self.crossed_player = True
            return True
        else:
            return False

class Pipes:
    CORRESPONDING_PIPE_DISTANCE = 150
    PIPE_CREATION_HEIGHT_RANGE = (150, 250)
    def __init__(self, screenw, screenh, renderer):
        self.screenw, self.screenh = screenw, screenh
        self.renderer = renderer

        self.load_textures()
        self.load_sound()

        self.is_game_started = False
        self.current_pipe_id = 0
        self.last_pipe = None

        self.pipes = {}

    def load_textures(self):
        pipe_up_image = pygame.image.load(path.join(settings.ASSETS_PATH, "pipe_up.png"))
        self.pipe_up_texture = sdl2.Texture.from_surface(self.renderer, pipe_up_image)

        pipe_down_image = pygame.image.load(path.join(settings.ASSETS_PATH, "pipe_down.png"))
        self.pipe_down_texture = sdl2.Texture.from_surface(self.renderer, pipe_down_image)

        self.rect = self.pipe_down_texture.get_rect()

    def load_sound(self):
        self.crash_sound = pygame.mixer.Sound(
            path.join(settings.ASSETS_PATH, "crash.wav")
            )
        self.score_sound = pygame.mixer.Sound(
            path.join(settings.ASSETS_PATH, "score.wav")
            )

    def physics(self, dt, player):
        self.pipe_creation(player.state)
        pipes_to_delete = []
        for _id in self.pipes:
            self.pipes[_id].physics(dt, player.VELX, player.state)
            if self.pipes[_id].check_if_crossed_player(player.POSX):
                player.score += 1
                self.score_sound.play()
            if self.pipes[_id].collide_with_player(player.rect):
                if player.state not in ("collided", "died"):
                    player.state = "collided"
                    self.crash_sound.play()
            if self.pipes[_id].is_out_of_screen():
                pipes_to_delete.append(_id)
        for _id in pipes_to_delete:
            self.pipes.pop(_id)

    def draw(self):
        for _id in self.pipes:
            self.pipes[_id].draw(
                self.renderer,
                self.pipe_up_texture,
                self.pipe_down_texture
                )

    def reset(self):
        self.is_game_started = False
        self.current_pipe_id = 0
        self.last_pipe = None

        self.pipes = {}

    def pipe_creation(self, player_state):
        if not self.is_game_started:
            if player_state == "moving":
                self.is_game_started = True
                self.last_pipe = self.create_pipe()
        else:
            if self.screenw - self.last_pipe.pos.x >= self.CORRESPONDING_PIPE_DISTANCE:
                self.last_pipe = self.create_pipe()

    def create_pipe(self):
        pipe = Pipe(
            self.current_pipe_id,
            pygame.Vector2(self.screenw, random.randint(*self.PIPE_CREATION_HEIGHT_RANGE)),
            pygame.Rect(self.rect))
        self.pipes[self.current_pipe_id] = pipe
        self.current_pipe_id += 1
        return pipe
