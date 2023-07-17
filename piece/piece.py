import pygame
from abc import ABC, abstractmethod
import sys

sys.path.append("..")

from constants import *


class Piece(ABC):
    def __init__(self, color: tuple[int, int, int]) -> None:
        self.color: tuple[int, int, int] = color

    @abstractmethod
    def draw(self, screen) -> None:
        pass

    @abstractmethod
    def rotate(self) -> None:
        pass

    @abstractmethod
    def drop(self) -> None:
        pass

    @abstractmethod
    def move(self, direction) -> None:
        pass
