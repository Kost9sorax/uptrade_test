from django.urls import re_path, include
from django.contrib import admin

urlpatterns = [
    re_path(r'^main_app/', include('main_app.urls')),
    re_path(r'^admin/', admin.site.urls),
]
