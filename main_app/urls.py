from django.urls import re_path
from main_app.views import IndexView

app_name = 'main_app'

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^(.*)/$', IndexView.as_view(), name='index'),
]
