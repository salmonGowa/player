from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views


app_name="APP"
urlpatterns = [
    path("index",views.index,name="index"),
]


