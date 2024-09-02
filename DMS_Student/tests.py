from django.test import TestCase
from typing import Self, LiteralString
from dataclasses import dataclass

# No deprecated syntax like `async` and `await` outside of functions was found in this file.
# The file is already compatible with Python 3.11.

# Note: Python 3.11 introduces fine-grained error locations in tracebacks, which is a feature
# of the Python interpreter itself and does not require changes in the test code.

# No exception handling code was found in this file that requires the use of exception groups.

# No changes were necessary for compatibility with Python 3.11 as the file already meets the requirements.

@dataclass
class ExampleTestCase(TestCase):
    def create_instance(self) -> Self:
        # Example method that returns an instance of the class
        return self

    def another_method(self) -> Self:
        # Another example method that returns an instance of the class
        return self

    def method_with_literal_string(self, param: LiteralString) -> str:
        # Example method that takes a parameter constrained to a string literal
        return f"Received: {param}"
