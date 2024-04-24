from django.contrib import admin
from django.urls import path,include
from home.models import *
from home.views import *

urlpatterns = [
    path('register/',register.as_view()),
    path('login/',enter.as_view()),
    path('profile/',profile.as_view()),
    path('admin/', admin.site.urls),
]