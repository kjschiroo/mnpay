from django.conf.urls import url

from . import views

app_name = "wages"
urlpatterns = [
    url(r'^wages$', views.get_wages, name='get_wages'),
]
