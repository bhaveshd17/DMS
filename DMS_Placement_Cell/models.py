from django.db import models

# Create your models here.

# Note: The original code does not contain any specific Python 3.11 features or syntax that need to be addressed.
# However, if you are using Python 3.11, ensure that your Django version is compatible with it.
# Additionally, Python 3.11 introduces fine-grained error locations in tracebacks, which is a runtime feature and does not require code changes here.

# No specific code changes are needed for compatibility with Python 3.11 in this file.
# The use of exception groups with the `except*` syntax is not applicable here as there are no exceptions being handled in this file.

# Implementing the `Self` type for class methods returning an instance of the class
from typing import Self

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)

    def clone(self) -> Self:
        """
        Create a clone of the current instance.
        """
        return ExampleModel(name=self.name)

    def update_name(self, new_name: str) -> Self:
        """
        Update the name of the instance and return the instance.
        """
        self.name = new_name
        return self
