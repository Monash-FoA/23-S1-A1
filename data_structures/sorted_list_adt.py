"""
    SortedList ADT.
    Defines a generic abstract sorted list with the standard methods.
    Items to store should be of time ListItem.
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')
K = TypeVar('K')

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

class ListItem(Generic[T, K]):
    """ Items to be stored in a list, including the value and the key used for sorting. """
    def __init__(self, value: T, key: K):
        self.value = value
        self.key = key

    def __str__(self) -> str:
        return '({0}, {1})'.format(self.value, self.key)

class SortedList(ABC, Generic[T]):
    """ Abstract class for a generic SortedList. """
    def __init__(self) -> None:
        """ Basic SortedList object initialiser. """
        self.length = 0

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        pass

    @abstractmethod
    def __setitem__(self, index: int, item: ListItem) -> None:
        """ Magic method. Insert the item at a given position,
            if possible (!). Shift the following elements to the right.
        """
        pass

    def __len__(self) -> int:
        """ Return the size of the list. """
        return self.length

    def __str__(self) -> str:
        """ Magic method constructing a string representation of the list object. """
        result = '['
        for i in range(len(self)):
            if i > 0:
                result += ', '
            result += str(self[i]) if type(self[i]) != str else "'{0}'".format(self[i])
        result += ']'
        return result

    @abstractmethod
    def delete_at_index(self, index: int) -> ListItem:
        """ Delete item at a given position. """
        pass

    @abstractmethod
    def index(self, item: ListItem) -> int:
        """ Find the position of a given item in the list. """
        pass

    def remove(self, item: T) -> None:
        """ Remove an item from the list. """
        index = self.index(item)
        self.delete_at_index(index)

    def is_empty(self) -> bool:
        """ Check if the list of empty. """
        return len(self) == 0

    def clear(self) -> None:
        """ Clear the list. """
        self.length = 0

    @abstractmethod
    def add(self, item: ListItem) -> None:
        """ Add new element to the list. """




        pass


