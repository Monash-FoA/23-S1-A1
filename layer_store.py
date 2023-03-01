from __future__ import annotations
from abc import ABC, abstractmethod
from layer_util import Layer
from data_structures.stack_adt import ArrayStack, Stack


class LayerStore(ABC):

   def __init__(self) -> None:
       pass

   @abstractmethod
   def add(self, layer: Layer) -> bool:
       """
       Add a layer to the store.
       Returns true if the LayerStore was actually changed.
       """
       pass

   @abstractmethod
   def get_color(self, start, timestamp, x, y) -> tuple[int, int, int]:
       """
       Returns the colour this square should show, given the current layers.
       """
       pass

   @abstractmethod
   def erase(self, layer: Layer) -> bool:
       """
       Complete the erase action with this layer
       Returns true if the LayerStore was actually changed.
       """
       pass

   @abstractmethod
   def special(self):
       """
       Special mode. Different for each store implementation.
       """
       pass


class SetLayerStore(LayerStore):
   """
   Set layer store. A single layer can be stored at a time (or nothing at all)
   - add: Set the single layer.
   - erase: Remove the single layer. Ignore what is currently selected.
   - special: Invert the colour output.
   """

   def __init__(self) -> None:
       self.layers: Stack[Layer] = ArrayStack(100)
       self.inverted = False

   def add(self, layer: Layer) -> bool:
       """
       Add a layer to the store.
       Returns true if the LayerStore was actually changed.
       """
       if len(self.layers) > 0 and self.layers.peek() == layer:
           return False
       self.layers.push(layer)
       return True

   def get_color(self, start, timestamp, x, y) -> tuple[int, int, int]:
       """
       Returns the colour this square should show, given the current layers.
       """
       if len(self.layers) > 0:
           color = self.layers.peek().apply(start, timestamp, x, y)
           if self.inverted:
               return (255 - color[0], 255 - color[1], 255 - color[2])
           else:
               return color
       else:
           return (255, 255, 255)

   def erase(self, layer: Layer) -> bool:
       """
       Complete the erase action with this layer
       Returns true if the LayerStore was actually changed.
       """
       if len(self.layers) > 0 and self.layers.peek() == layer:
           self.layers.pop()
           return True
       return False

   def special(self):
       """
       Special mode. Different for each store implementation.
       """
       self.inverted = not self.inverted
