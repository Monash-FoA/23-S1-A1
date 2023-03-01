from __future__ import annotations
from array_sorted_list import ArraySortedList
from layer_store import SetLayerStore

class Grid:
    DRAW_STYLE_SET = "SET"
    DRAW_STYLE_ADD = "ADD"
    DRAW_STYLE_SEQUENCE = "SEQUENCE"
    DRAW_STYLE_OPTIONS = (
        DRAW_STYLE_SET,
        DRAW_STYLE_ADD,
        DRAW_STYLE_SEQUENCE
    )

    DEFAULT_BRUSH_SIZE = 2
    MAX_BRUSH = 5
    MIN_BRUSH = 0

    def __init__(self, draw_style, x, y) -> None:
        """
        Initialise the grid object.
        - draw_style:
            The style with which colours will be drawn.
            Should be one of DRAW_STYLE_OPTIONS
            This draw style determines the LayerStore used on each grid square.
        - x, y: The dimensions of the grid.

        Should also intialise the brush size to the DEFAULT provided as a class variable.
        """
        self.draw_style = draw_style
        self.width = x
        self.height = y
        self.brush_size = self.DEFAULT_BRUSH_SIZE
        self.grid = [[None for _ in range(y)] for _ in range(x)]
        self.layer_store = SetLayerStore()

        # set layer_store for each grid square based on the draw_style
        if self.draw_style == self.DRAW_STYLE_SET:
            for i in range(x):
                for j in range(y):
                    self.grid[i][j] = self.layer_store
        elif self.draw_style == self.DRAW_STYLE_ADD:
            for i in range(x):
                for j in range(y):
                    self.grid[i][j] = ArraySortedList(1)
        elif self.draw_style == self.DRAW_STYLE_SEQUENCE:
            for i in range(x):
                for j in range(y):
                    self.grid[i][j] = ArraySortedList()


    def increase_brush_size(self):
        """
        Increases the size of the brush by 1,
        if the brush size is already MAX_BRUSH,
        then do nothing.
        """
        if self.brush_size < self.MAX_BRUSH:
            self.brush_size += 1

    def decrease_brush_size(self):
        """
        Decreases the size of the brush by 1,
        if the brush size is already MIN_BRUSH,
        then do nothing.
        """
        if self.brush_size > self.MIN_BRUSH:
            self.brush_size -= 1

    def special(self):
        """
        Activate the special affect on all grid squares.
        """
        for x in range(self.width):
            for y in range(self.height):
                layer_store = self.grid[x][y]
                if layer_store is not None:
                    layer_store.set_special()

    def __getitem__(self, position):
        return self.grid[position[0]][position[1]]

    def __setitem__(self, position, item):
        self.grid[position[0]][position[1]] = item
