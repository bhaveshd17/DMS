from django.test import TestCase

# Create your tests here.

# Note: Python 3.11 introduces fine-grained error locations in tracebacks, 
# which provide specific line numbers and code snippets in error messages.
# This feature is automatically utilized when running tests with Django's TestCase.

# Example of handling multiple exceptions using exception groups in Python 3.11
def example_function():
    try:
        # Some code that may raise multiple exceptions
        pass
    except* (ValueError, TypeError) as e:
        # Handle ValueError and TypeError exceptions
        print(f"Handled exceptions: {e}")
    except Exception as e:
        # Handle any other exceptions
        print(f"Unhandled exception: {e}")
