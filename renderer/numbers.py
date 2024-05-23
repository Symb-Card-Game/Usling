import pygame as pg

def render_hp(players, size: tuple[int, int]):

    hp_surface = pg.Surface((size[0], size[1]), pg.SRCALPHA, 32)

    initial_placement = 10
    size_offset = 50

    if pg.font:
        font = pg.font.Font(None, 64)
        for i, player in enumerate(players):
            text = font.render(str(player.hp), True, (10, 10, 10))
            textpos = text.get_rect(centerx = size[0] / 2, y = initial_placement + (i * (size[1] - initial_placement - size_offset)))
            hp_surface.blit(text, textpos)
    return hp_surface
