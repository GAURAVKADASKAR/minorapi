from django.contrib import admin
from django.urls import path,include
from home.models import *
from home.views import *

urlpatterns = [
    path('register/',register.as_view()),
    path('login/',enter.as_view()),
    path('profile/',profile.as_view()),
    path('feedback/',feedback.as_view()),
    path('viewbeds/',filterbeds.as_view()),
    path('view_beds/<id>/',view_beds),
    path('viewhospital/',viewhospital.as_view()),
    path('viewrequest/',viewrequest.as_view()),
    path('get_hospital_by_id/<id>/',get_hospital_by_id),
    path('reject/<id>/',rejectrequest),
    path('select/<id>/',selectrequest),
    path('request_for_beds/',requst_for_beds.as_view()),
    path('discharge/<id>/',discharge),
    path('viewpatient/',finalinfo),
    path('admin/', admin.site.urls),
]