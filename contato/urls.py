from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contato, name='contato'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
