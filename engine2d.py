import pygame


class Engine2D:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.canvas = pygame.display.set_mode((self.width, self.height))
        self.color = (0, 0, 0)
        pygame.display.set_caption("2D Engine")
        self.figures = []

    def change_color(self, color):
        self.color = color

    @staticmethod
    def update_canvas():
        pygame.display.flip()

    def clear_canvas(self):
        self.figures.clear()
        self.canvas.fill((0, 0, 0))
        self.update_canvas()

    def add_figure(self, figure):
        self.figures.append(figure)

    def draw(self, clear=True):
        for figure in self.figures:
            figure.draw()
        self.update_canvas()
        if clear:
            self.clear_canvas()


class Circle:
    def __init__(self, position, radius, engine, color=None):
        self.position = position
        self.radius = radius
        self.engine = engine
        if color:
            self.color = color
        else:
            self.color = engine.color

    def draw(self):
        pygame.draw.circle(self.engine.canvas, self.color, self.position, self.radius)
        print(f"Drawing Circle: {self.position} with radius {self.radius} and color {self.color}")


class Triangle:
    def __init__(self, points, engine, color=None):
        self.points = points
        self.engine = engine
        if color:
            self.color = color
        else:
            self.color = engine.color

    def draw(self):
        pygame.draw.polygon(self.engine.canvas, self.color, self.points)
        print(f"Drawing Triangle: {self.points} with color {self.color}")


class Rectangle:
    def __init__(self, position, size, engine, color=None):
        self.position = position
        self.size = size
        self.engine = engine
        if color:
            self.color = color
        else:
            self.color = engine.color

    def draw(self):
        rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        pygame.draw.rect(self.engine.canvas, self.color, rect)
        print(f"Drawing Rectangle: {self.position} with size {self.size} and color {self.color}")


engine = Engine2D(700, 600)

red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

engine.change_color(red)
circle = Circle((100, 100), 50, engine)
engine.add_figure(circle)

engine.change_color(yellow)
rectangle = Rectangle((220, 220), (300, 100), engine)
engine.add_figure(rectangle)

engine.change_color(red)
circle = Circle((350, 350), 30, engine)
engine.add_figure(circle)

engine.change_color(green)
triangle = Triangle([(400, 100), (300, 200), (500, 200)], engine)
engine.add_figure(triangle)

engine.draw()
