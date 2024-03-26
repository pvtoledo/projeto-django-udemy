from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/<int:post_id>/detalhe_post', views.detalhe_post, name='detalhe_post'),
    path('posts/<int:post_id>/comentarios', views.comentar, name='comentarios'),
    path('posts/comentarios/<int:post_id>', views.comentar_post, name='comentar_post_htmx'),
    path('posts/comentarios/deletar/<int:comentario_id>', views.deletar_comentario, name='deletar_comentario_htmx'),
    path('posts/comentarios/editar/<int:comentario_id>', views.editar_comentario, name='editar_comentario_htmx'),
    path('blog', views.blog, name='blog')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
