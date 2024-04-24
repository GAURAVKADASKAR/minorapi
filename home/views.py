from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from home.models import *
from django.conf import settings
from home.serializer import *
from home.models import *


# Create your views here.

class register(APIView):
    def post(self,request):
        serializer=registerserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':200,'message':serializer.errors})
        subject="Account Verification for CareConnect"
        message="Dear User,\n\n Thank you for registering with CareConnect.\n\n To complete the registration process and ensure the security of your account, please verify your email address by clicking the link below: \n http://127.0.0.1:8000/login/ \n\n If you are unable to click the link above, please copy and paste it into your web browser's address bar.\n\n Once your email address has been verified, you will gain full access to our platform and its features. \n\n If you did not register with CareConnect, please ignore this email.\n\n Thank you for choosing CareConnect. If you have any questions or need further assistance, please don't hesitate to contact us at CareConnect.support@gmail.com.\n\n Best regards"
        from_email=settings.EMAIL_HOST_USER
        user=request.data['email']
        recipient_list=[user]
        send_mail(subject,message,from_email,recipient_list)
        serializer.save()
        return Response({'status':200,'message':serializer.data})
class enter(APIView):
    def post(self,request):
        username=request.data['username']
        password=request.data['password']
        user=authenticate(username=username,password=password)
        if user is None:
            return Response({'status':200,'message':'invlaid username and password'})
        request.session['username']=request.data['username']
        request.session.set_expiry(30)
        print(request.session['username'])
        return Response({'status':200,'message':'login'})
class profile(APIView):
    def get(self,request):
        if request.session.has_key('username'):
            user=request.session['username']
            obj=registration.objects.filter(email=user)
            serializer=profileserializer(obj,many=True)
            return Response({'status':200,'message':serializer.data})
        else:
            return Response({'status':200,'message':'login required'})
        
            
    
    
