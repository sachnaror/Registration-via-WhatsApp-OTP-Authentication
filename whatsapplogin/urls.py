# my_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    # path('', include('home.urls')),
]
