import pygame
from pygame.examples.setmodescale import clock

import game_regulations

screen = pygame.display.set_mode(game_regulations.SCREEN_WIDTH, game_regulations.SCREEN_HEIGHT)
pygame.display.set_caption("Target shooting")
clock = pygame.time.Clock()
font = pygame.font.Font('georgia', 36)


