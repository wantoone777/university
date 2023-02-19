from django.contrib import admin
from django.urls import path, include
from .settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from universitygo.views import to_universitygo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('universitygo/', include('universitygo.urls')),
    path('', to_universitygo),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
