from django.contrib import admin
from django.urls import path, include
from boristest.settings import MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL
from django.conf.urls.static import static
from app.views import FileUploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/upload/', FileUploadView.as_view()),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


