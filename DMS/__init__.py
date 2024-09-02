# DMS/__init__.py

# Import necessary modules
import logging

# Initialize logger
logger = logging.getLogger(__name__)

def process_data(data):
    try:
        # Simulate processing data
        result = data / 0  # This will raise a ZeroDivisionError
    except (ZeroDivisionError, TypeError) as e:
        # Add note to exception (Python 3.11+ feature)
        e.add_note("Error occurred during data processing.")
        logger.error(f"An error occurred: {e}")
        # Handle specific exceptions
        if isinstance(e, ZeroDivisionError):
            logger.error("Cannot divide by zero.")
        elif isinstance(e, TypeError):
            logger.error("Invalid data type for division.")
    except Exception as e:
        # Add note to exception (Python 3.11+ feature)
        e.add_note("Unexpected error during data processing.")
        logger.error(f"An unexpected error occurred: {e}")
    else:
        logger.info("Data processed successfully.")
        return result
    finally:
        logger.info("Process completed.")
