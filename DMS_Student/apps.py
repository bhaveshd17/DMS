from django.apps import AppConfig

class DmsStudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DMS_Student'

    # Python 3.11 compatibility is inherently supported as this code does not use any deprecated features.
    # If debugging errors, utilize fine-grained error locations in tracebacks to provide specific line numbers and code snippets in error messages.
