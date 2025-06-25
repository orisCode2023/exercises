import pygame
import intities
import colors
import game_regulations
import game_panel
import random


def check_collision():
    distance = ((intities.ball_x - intities.target_x) ** 2 + (intities.ball_y - intities.target_y) ** 2) ** 0.5
    if distance <= game_regulations.BALL_RADIUS + game_regulations.TARGET_RADIUS:
        intities.score += 1
    intities.target_x = random.randint(50, 750)
    intities.target_y = random.randint(50, 450)


def draw_screen():
    game_panel.screen.fill(colors.BLACK)
    pygame.draw.circle(game_panel.screen, colors.RED, (intities.ball_x, intities.ball_y), game_regulations.BALL_RADIUS)
    pygame.draw.circle(game_panel.screen, colors.GREEN, (intities.target_x, intities.target_y),
                       game_regulations.TARGET_RADIUS)

def score_on_screen():
    text = game_panel.font.render(f"Score: {intities.score}" , True, colors.WHITE)
    game_panel.screen.blit(text, (10, 10))


def loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                intities.ball_x, intities.ball_y = pygame.mouse.get_pos()

        check_collision()
        draw_screen()
        score_on_screen()
        pygame.display.flip()
        game_panel.clock.tick(game_regulations.FPS)
