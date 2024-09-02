from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DMS_Student.urls')),
    path('placement_cell/', include('DMS_Placement_Cell.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Note: Python 3.11 introduces fine-grained error locations in tracebacks by default.
# No changes are needed in this file to utilize this feature.
