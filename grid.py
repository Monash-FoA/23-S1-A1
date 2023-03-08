
from __future__ import annotations
from data_structures import stack_adt
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

    def __init__(self, draw_style, x: int, y: int) -> None:
        """
        Initialise the grid object.
        - draw_style:
            The style with which colours will be drawn.
            Should be one of DRAW_STYLE_OPTIONS
            This draw style determines the LayerStore used on each grid square.
        - x, y: The dimensions of the grid.

        Should also intialise the brush size to the DEFAULT provided as a class variable.
        """
        self.draw_style = Grid.DRAW_STYLE_SET
        self.x = x
        self.y = y
        self.brush_size = Grid.DEFAULT_BRUSH_SIZE

        def create_grid():
            row = ()
            grid = ()

            y = 0
            while y != self.y:
                for i in range(0, self.x+1):
                    row += (SetLayerStore(i,y),)


                y += 1
                grid += (row,)

            return grid


        self.grid = create_grid()

    def __getitem__(self, key):
        return self.grid[key]


    def increase_brush_size(self):
        """
        Increases the size of the brush by 1,
        if the brush size is already MAX_BRUSH,
        then do nothing.
        """
        if self.brush_size is not Grid.MAX_BRUSH:
            self.brush_size += 1

        return self.brush_size

        raise NotImplementedError()

    def decrease_brush_size(self):
        """
        Decreases the size of the brush by 1,
        if the brush size is already MIN_BRUSH,
        then do nothing.
        """

        if self.brush_size is not Grid.MIN_BRUSH:
            self.brush_size -= 1

        return self.brush_size
        raise NotImplementedError()

    def special(self):
        """
        Activate the special affect on all grid squares.
        """
        raise NotImplementedError()

if __name__ == "__main__":
    print(Grid(1,2,3)[1][4])




