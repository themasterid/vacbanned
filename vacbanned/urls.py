from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('getvac.urls', namespace='getvac')),
    path('admin/', admin.site.urls),
]
