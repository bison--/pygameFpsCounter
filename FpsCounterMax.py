import pygame


class FpsCounterMax:

    def __init__(self, screen):
        self.__screen = screen
        self.font = pygame.font.SysFont("MS Comic Sans,Comic Neue", 30)
        self.position = (10, 10)
        self.color = (245, 101, 44)  # orange
        self.__calculation_time = 1000
        self.time_point_count = 0
        self.time_point_amount = 600
        self.time_points = []
        self.fps_point_amount = 60
        self.fps_points = []
        self.time_since_last_calculation = 0
        self.fps_min = -1
        self.fps_max = -1
        self.fps_template = 'FPS: {0} AVG: {1:.2f} MIN: {2} MAX: {3}'
        self.fps_text = 'FPS: - AVG: - MIN: - MAX: -'

    def _calculate(self):
        time_points_collected = len(self.time_points)

        self.fps_points.append(self.time_point_count)

        if time_points_collected > self.time_point_amount:
            self.time_points.pop(0)

        if len(self.fps_points) > self.fps_point_amount:
            self.fps_points.pop(0)

        if self.fps_min == -1:
            self.fps_min = self.time_point_count
            self.fps_max = self.time_point_count
        elif self.time_point_count < self.fps_min:
            self.fps_min = self.time_point_count
        elif self.time_point_count > self.fps_max:
            self.fps_max = self.time_point_count

        all_fps = 0
        for fps_point in self.fps_points:
            all_fps += fps_point

        self.fps_text = self.fps_template.format(
            self.time_point_count,
            all_fps / len(self.fps_points),
            self.fps_min,
            self.fps_max
        )

        self.time_point_count = 0
        self.time_since_last_calculation = 0

    def _render_text(self):
        self.__screen.blit(self.font.render(self.fps_text, False, self.color), self.position)

    def render_fps(self, time_passed):
        self.time_points.append(time_passed)
        self.time_point_count += 1
        self.time_since_last_calculation += time_passed

        if self.time_since_last_calculation >= self.__calculation_time:
            self._calculate()

        self._render_text()
