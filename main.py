import pygame
import pygame._sdl2 as sdl2

from player import Player
from pipe import Pipes
from scene import Scene
from menus import MainMenu


pygame.init()

__ANDROID__ = True
try:
    import android
except ImportError:
    __ANDROID__ = False


MONITORW = 1920
MONITORH = 1080
SCREENW = 512
SCREENH = 384

if __ANDROID__:
    window = sdl2.Window("Flappy Bird", (MONITORW, MONITORH), fullscreen = True)
else:
    window = sdl2.Window("Flappy Bird", (SCREENW, SCREENH))


renderer = sdl2.Renderer(window, accelerated = True)
if __ANDROID__:
    renderer.logical_size = SCREENW, SCREENH


# Main part of the game starts from here
FPS = 6000

rng = True
state = "not started"
clock = pygame.time.Clock()

player = Player(SCREENW, SCREENH, renderer)
pipes = Pipes(SCREENW, SCREENH, renderer)
scene = Scene(SCREENW, SCREENH, renderer, player.POSX)
main_menu = MainMenu(SCREENW, SCREENH, renderer)

while rng:
    dt = clock.tick(FPS) / 1000
    # print(clock.get_fps())

    # The cool pygame(SDL) event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rng = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                rng = False
        player.events(event)

    # Handle the events
    player.physics(dt, scene.base_rect.h)
    pipes.physics(dt, player)
    scene.physics(dt, player.pos.x)

    # Draw
    renderer.draw_color = (0, 0, 0, 255) # Set the draw colour
    renderer.clear() # Fill the screen with the set draw colour
    scene.draw_bg()
    pipes.draw()
    player.draw()
    scene.draw_base()
    if player.state == "idle":
        main_menu.draw()
    renderer.present() # Update the screen
