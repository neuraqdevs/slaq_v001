from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'voiceapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    # path('result/', views.result, name='result'), 
    # path('success/', views.success, name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)