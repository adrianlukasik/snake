import pygame
import sys
from parameters import *
from snake import Snake
from element import Element


class Game(object):

    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('Snake')

        tps_clock = pygame.time.Clock()
        tps_delta = 0.0
        snake = Snake()
        item = Element(snake)
        key = pygame.K_d

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and key != pygame.K_w:
                    key = pygame.K_s
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w and key != pygame.K_s:
                    key = pygame.K_w
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d and key != pygame.K_a:
                    key = pygame.K_d
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_a and key != pygame.K_d:
                    key = pygame.K_a

            # Ticking
            tps_delta += tps_clock.tick() / 1000.0
            while tps_delta > 1 / TPS_MAX:
                snake.move(key)

                if snake.isColision():
                    sys.exit(0)

                if item.isColision(snake):
                    snake.extend()
                    item = Element(snake)

                tps_delta -= 1 / TPS_MAX

            # Drawing
            screen.fill(BLACK)
            item.draw(screen, RED, DARK_RED)
            snake.draw(screen)
            pygame.display.flip()

Game()
