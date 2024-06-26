
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from quiz.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("quiz/", include("quiz.urls")),
    path("", index, name="index"),
    path(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
