from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DMS_Student.urls')),
<<<<<<< HEAD
    path('placement_cell/', include('DMS_Placement_Cell.urls')),
=======
    path('company/',include('DMS_Company.urls')),
>>>>>>> 408326523106c77293ff5435a75682c0ab5c7692
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)