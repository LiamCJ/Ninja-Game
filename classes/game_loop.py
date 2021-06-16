import pygame as pg

from main import Main

g = Main()
g.show_start_screen()
while g.running:
    g.new()
    g.game_over()

pg.quit()
