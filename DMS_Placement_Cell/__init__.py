# DMS_Placement_Cell/__init__.py

# This module is intended to be compatible with Python 3.11.
# Implementing the `Self` type for class methods returning an instance of the class.

from typing import Self, LiteralString
from dataclasses import dataclass

@dataclass
class ExampleClass:
    value: int

    def set_value(self, new_value: int) -> Self:
        self.value = new_value
        return self

    def increment_value(self) -> Self:
        self.value += 1
        return self

    def get_value(self) -> int:
        return self.value
