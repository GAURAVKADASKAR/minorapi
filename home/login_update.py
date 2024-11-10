from home.models import *
from rest_framework.response import Response


def update_login(name,login_value):
    
    obj=DoctorRegistration.objects.get(email=name)
    obj.login_status=login_value
    obj.save()
    
 
    return "successfull"

    