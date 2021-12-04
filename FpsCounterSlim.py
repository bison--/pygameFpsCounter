import time
import pygame


class FpsCounterSlim:

    def __init__(self, screen):
        self.__screen = screen
        self.font = pygame.font.SysFont("MS Comic Sans,Comic Neue", 30)
        self.position = (10, 10)
        self.color = (245, 101, 44)  # orange
        self.__next_calculation_time = time.time() + 1
        self.time_point_count = 0
        self.fps_template = 'FPS: {0}'
        self.fps_text = 'FPS: -'

    def _calculate(self):
        self.fps_text = self.fps_template.format(self.time_point_count)
        self.time_point_count = 0
        self.__next_calculation_time = time.time() + 1

    def _render_text(self):
        self.__screen.blit(self.font.render(self.fps_text, False, self.color), self.position)

    def render_fps(self):
        self.time_point_count += 1

        if time.time() >= self.__next_calculation_time:
            self._calculate()

        self._render_text()
