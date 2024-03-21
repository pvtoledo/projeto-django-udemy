from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('login/', include('autenticacao.urls')),
    path('contato/', include('contato.urls')),
    path('cursos/', include('cursos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
