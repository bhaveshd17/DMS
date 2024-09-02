#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from typing import TypeVar, Any

Ts = TypeVar('Ts', bound=Any)

def main(*args: Ts) -> None:
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DMS.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        exc.add_note(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
        raise
    execute_from_command_line(args)


if __name__ == '__main__':
    main(*sys.argv)
