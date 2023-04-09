import pygame
import pytest
from engine2d import Engine2D, Circle, Rectangle, Triangle


@pytest.fixture(scope="module")
def engine():
    pygame.init()
    return Engine2D(700, 600)


def test_engine_initialization(engine):
    """Verify that an instance of the Engine2D class is created without error and has the
    correct values for the width, height, and color"""
    assert engine.width == 700
    assert engine.height == 600
    assert engine.color == (0, 0, 0)
    assert len(engine.figures) == 0


def test_engine_change_color(engine):
    """Verify that the change_color method changes the value of the color to the given one"""
    engine.change_color((255, 0, 0))
    assert engine.color == (255, 0, 0)


def test_engine_add_figure(engine):
    """Verify that the add_figure method adds a shape to the list of shapes"""
    circle = Circle((100, 100), 50, engine)
    engine.add_figure(circle)
    assert len(engine.figures) == 1
    assert engine.figures[0] == circle


def test_engine_draw(engine):
    """Verify that the draw method draws all the shapes on the canvas and calls the
    update_canvas and clear_canvas methods."""
    circle = Circle((100, 100), 50, engine)
    rectangle = Rectangle((220, 220), (300, 100), engine)
    engine.add_figure(circle)
    engine.add_figure(rectangle)
    engine.draw()
    assert pygame.display.get_caption()[0] == "2D Engine"
    assert pygame.display.get_surface().get_size() == (700, 600)
    assert len(engine.figures) == 0


def test_engine_draw_clear_false(engine):
    """Verify that the draw method draws all the shapes on the canvas and calls the
    update_canvas"""
    circle = Circle((100, 100), 50, engine)
    rectangle = Rectangle((220, 220), (300, 100), engine)
    engine.add_figure(circle)
    engine.add_figure(rectangle)
    engine.draw(clear=False)
    assert len(engine.figures) == 2


def test_engine_clear_canvas(engine):
    """Verify that the clear_canvas method clears the canvas"""
    circle = Circle((100, 100), 50, engine)
    engine.add_figure(circle)
    engine.draw()
    engine.clear_canvas()
    assert len(engine.figures) == 0


def test_circle_creation(engine):
    """Verify that Circle is created without error and has the correct position, radius and color"""
    circle = Circle((100, 100), 50, engine)
    assert circle.position == (100, 100)
    assert circle.radius == 50
    assert circle.color == engine.color


def test_circle_color_override(engine):
    """Verify that color of the Circle overrides correctly"""
    circle = Circle((100, 100), 50, engine, color=(255, 0, 0))
    assert circle.color == (255, 0, 0)


def test_triangle_creation(engine):
    """Verifies that Triangle is created without error and has the correct points and color"""
    triangle = Triangle([(400, 100), (300, 200), (500, 200)], engine)
    assert triangle.points == [(400, 100), (300, 200), (500, 200)]
    assert triangle.color == engine.color


def test_triangle_color_override(engine):
    """Verify that color of the Triangle overrides correctly"""
    triangle = Triangle([(400, 100), (300, 200), (500, 200)], engine, color=(0, 255, 0))
    assert triangle.color == (0, 255, 0)


def test_rectangle_creation(engine):
    """Verifies that Rectangle is created without error and has the correct position, size and color"""
    rectangle = Rectangle((220, 220), (300, 100), engine)
    assert rectangle.position == (220, 220)
    assert rectangle.size == (300, 100)
    assert rectangle.color == engine.color


def test_rectangle_color_override(engine):
    """Verify that color of the Rectangle overrides correctly"""
    rectangle = Rectangle((220, 220), (300, 100), engine, color=(0, 0, 255))
    assert rectangle.color == (0, 0, 255)
