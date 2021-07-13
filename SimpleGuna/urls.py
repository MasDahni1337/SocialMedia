from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sg_sosial import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sg_sosial.urls')),
    path('keluar/', views.keluar, name='keluar'),
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('', views.masuk, name='masuk'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)