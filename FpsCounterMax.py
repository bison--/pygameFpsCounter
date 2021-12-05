import time
import statistics
import pygame


class FpsCounterMax:

    def __init__(self, screen):
        self.__screen = screen
        self.font_size = 30
        self.font = pygame.font.SysFont("MS Comic Sans,Comic Neue", self.font_size)
        self.position = (10, 10)
        self.color = (245, 101, 44)  # orange
        self.__next_calculation_time = time.time() + 1
        self.time_point_count = 0
        self.fps_point_amount = 60
        self.fps_points = []
        self.time_since_last_calculation = 0
        self.fps_min = -1
        self.fps_max = -1
        self.fps_template1 = 'FPS: {0} AVG: {1:.2f} MIN: {2} MAX: {3}'
        self.fps_template2 = 'MEDIAN: {0:.2f} DEVIATION: {1:.2f}'
        self.fps_text1 = 'FPS: - AVG: - MIN: - MAX: -'
        self.fps_text2 = 'MEDIAN: - DEVIATION: -'

    def _calculate(self):
        self.fps_points.append(self.time_point_count)

        if len(self.fps_points) > self.fps_point_amount:
            self.fps_points.pop(0)

        median = 0
        deviation = 0
        if len(self.fps_points) >= 2:
            median = statistics.median(self.fps_points)
            deviation = statistics.stdev(self.fps_points)

        self.fps_text1 = self.fps_template1.format(
            self.time_point_count,
            sum(self.fps_points) / len(self.fps_points),
            min(self.fps_points),
            max(self.fps_points),
            median,
            deviation
        )
        self.fps_text2 = self.fps_template2.format(
            median,
            deviation
        )

        self.time_point_count = 0
        self.__next_calculation_time = time.time() + 1

    def _render_text(self):
        self.__screen.blit(self.font.render(self.fps_text1, False, self.color), self.position)
        self.__screen.blit(
            self.font.render(self.fps_text2, False, self.color),
            (self.position[0], self.position[1] + self.font_size)
        )

    def render_fps(self):
        self.time_point_count += 1

        if time.time() >= self.__next_calculation_time:
            self._calculate()

        self._render_text()
