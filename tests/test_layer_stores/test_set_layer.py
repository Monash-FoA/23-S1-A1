import unittest
from ed_utils.decorators import number

from layer_store import SetLayerStore
from layers import black, lighten, rainbow, invert

class TestSetLayer(unittest.TestCase):

    @number("1.1")
    def test_no_layer(self):
        s = SetLayerStore()
        for color in [
            (255, 255, 255),
            (0, 0, 0),
            (255, 0, 255),
        ]:
            self.assertEqual(s.get_color(color, 0, 1, 1), color)

    @number("1.2")
    def test_layers(self):
        s = SetLayerStore()
        s.add(black)
        self.assertEqual(s.get_color((20, 20, 20), 40, 0, 0), (0, 0, 0))
        # This should set it to light the background, not black.
        s.add(lighten)
        self.assertEqual(s.get_color((100, 100, 100), 0, 20, 40), (140, 140, 140))

    @number("1.3")
    def test_erase(self):
        s = SetLayerStore()
        s.add(black)
        s.erase(lighten)
        self.assertEqual(s.get_color((25, 25, 25), 24, 4, 100), (25, 25, 25))

    @number("1.4")
    def test_special(self):
        s = SetLayerStore()
        s.add(lighten)
        self.assertEqual(s.get_color((100, 100, 100), 0, 0, 0), (140, 140, 140))
        s.special()
        self.assertEqual(s.get_color((100, 100, 100), 0, 0, 0), (255-140, 255-140, 255-140))
        s.special()
        self.assertEqual(s.get_color((100, 100, 100), 0, 0, 0), (140, 140, 140))

    @number("1.5")
    def test_example(self):
        s = SetLayerStore()
        s.add(rainbow)
        self.assertEqual(s.get_color((0, 0, 0), 7, 0, 0), (91, 214, 104))
        s.add(lighten)
        self.assertEqual(s.get_color((0, 0, 0), 7, 0, 0), (40, 40, 40))
        s.erase(invert)
        self.assertEqual(s.get_color((0, 0, 0), 7, 0, 0), (0, 0, 0))
        s.add(invert)
        self.assertEqual(s.get_color((0, 0, 0), 7, 0, 0), (255, 255, 255))
