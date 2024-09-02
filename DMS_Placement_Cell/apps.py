from django.apps import AppConfig

class DmsPlacementCellConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DMS_Placement_Cell'

    # Python 3.11 introduces fine-grained error locations in tracebacks by default.
    # No changes are needed in this file to utilize this feature.
