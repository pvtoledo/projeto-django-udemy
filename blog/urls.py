from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<int:post_id>/detalhe_post', views.detalhe_post, name='detalhe_post')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
