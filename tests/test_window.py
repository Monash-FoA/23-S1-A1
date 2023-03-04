import unittest
from ed_utils.decorators import number

from layers import green, red, blue
from grid import Grid
from main import MyWindow

class FakeWindow:
    def __init__(self, grid: Grid):
        self.grid = grid

FakeWindow.on_init = MyWindow.on_init
FakeWindow.on_reset = MyWindow.on_reset
FakeWindow.on_paint = MyWindow.on_paint
FakeWindow.on_increase_brush_size = MyWindow.on_increase_brush_size
FakeWindow.on_decrease_brush_size = MyWindow.on_decrease_brush_size

class TestGrid(unittest.TestCase):

    @number("6.1")
    def test_basic(self):
        grid = Grid(Grid.DRAW_STYLE_SET, 5, 5)
        control_grid = Grid(Grid.DRAW_STYLE_SET, 5, 5)

        fw = FakeWindow(grid)
        fw.on_init()
        fw.on_reset()
        # Check default brush size of 2
        fw.on_paint(red, 2, 2)
        expected_change = [
            (2, 2),  # distance 0
            (1, 2), (3, 2), (2, 1), (2, 3),  # distance 1
            (0, 2), (1, 1), (2, 0), (3, 1), (4, 2), (3, 3), (2, 4), (1, 3),  # distance 2
        ]
        for x, y in expected_change:
            control_grid[x][y].add(red)

        self.assertGridEqual(grid, control_grid)

    @number("6.2")
    def test_increase_decrease(self):
        grid = Grid(Grid.DRAW_STYLE_SET, 5, 5)
        control_grid = Grid(Grid.DRAW_STYLE_SET, 5, 5)

        fw = FakeWindow(grid)
        fw.on_init()
        fw.on_reset()

        fw.on_decrease_brush_size()
        fw.on_decrease_brush_size()
        fw.on_paint(green, 1, 4)
        control_grid[1][4].add(green)
        self.assertGridEqual(grid, control_grid)

        # Decrease past 0 - not possible.
        fw.on_decrease_brush_size()
        fw.on_paint(green, 2, 2)
        control_grid[2][2].add(green)
        self.assertGridEqual(grid, control_grid)

        # Increase up to 4
        fw.on_increase_brush_size()
        fw.on_increase_brush_size()
        fw.on_increase_brush_size()
        fw.on_increase_brush_size()
        fw.on_paint(blue, 2, 2)
        for x in range(5):
            for y in range(5):
                control_grid[x][y].add(blue)

        self.assertGridEqual(grid, control_grid)

        # Increase past maximum
        fw.on_increase_brush_size()
        fw.on_increase_brush_size()
        fw.on_increase_brush_size()
        fw.on_increase_brush_size()
        fw.on_paint(green, 1, 1)
        for x in range(5):
            for y in range(5):
                control_grid[x][y].add(green)
        control_grid[4][4].add(blue)

        self.assertGridEqual(grid, control_grid)

    def assertGridEqual(self, grid1: Grid, grid2: Grid):
        for x in range(len(grid1.grid)):
            for y in range(len(grid1[x])):
                sq1 = grid1[x][y]
                sq2 = grid2[x][y]
                self.assertEqual(
                    sq1.get_color((0, 0, 0), 0, x, y),
                    sq2.get_color((0, 0, 0), 0, x, y),
                    "Grid not the same after apply has been made."
                )

