import pygame as pg

#Initialize the modules
pg.init()

#Define the screen properties
screen_size=swidth,sheight=1024,768
screen=pg.display.set_mode(screen_size)

font = pg.font.Font(r".\\Assets\\font_0.ttf", 40)
chars = {}
for i in range(10):
    text = font.render(str(i), False, "Red")
    rect = text.get_rect()
    bounding_rect = pg.Rect(0, 0, rect.h, rect.h)
    bounding_rect.center = rect.center
    width = bounding_rect.w
    height = bounding_rect.h
    chars[i] = (text, rect, bounding_rect)
surf = pg.Surface((width * len(chars), height))
surf.fill((255, 255, 255, 0))
print(width, height)
for i in chars:
    chars[i][2].x = i * width
    chars[i][1].center = chars[i][2].center
    surf.blit(chars[i][0], chars[i][1])
rng = True
while rng:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            rng = False
    screen.fill(0)
    for i in chars:
        chars[i][2].x = i * width
        chars[i][1].center = chars[i][2].center
        screen.blit(chars[i][0], chars[i][1])
    pg.display.update()
pg.image.save(surf.copy(), "text.png")

pg.quit()