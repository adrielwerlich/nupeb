from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf.urls.static import static

app_name = 'sitenupeb'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]