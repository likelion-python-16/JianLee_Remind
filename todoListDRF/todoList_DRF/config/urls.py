from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls), # , namespace=""
    path("todo/", include(("todo.urls", "todo"))),
    path("", lambda request: redirect("todo:todo_List")), # 127.0.0.1:8000/
    path("api-auth/", include("rest_framework.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('interaction/', include('interaction.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)