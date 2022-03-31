from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static


admin.site.site_header = "BappaOnline Admin"
admin.site.site_title = "BappaOnline Admin Dashboard"
admin.site.index_title = "Welcome to BappaOnline Admin Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
