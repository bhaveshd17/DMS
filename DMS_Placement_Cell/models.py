from django.db import models
from typing import Self, LiteralString
from dataclasses import dataclass

@dataclass
class ExampleModel(models.Model):
    name: models.CharField = models.CharField(max_length=100)

    def clone(self) -> Self:
        """
        Create a clone of the current instance.
        """
        return ExampleModel(name=self.name)

    def update_name(self, new_name: LiteralString) -> Self:
        """
        Update the name of the instance and return the instance.
        """
        self.name = new_name
        return self
