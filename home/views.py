from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from home.models import *
from django.conf import settings
from home.serializer import *
from home.models import *
from rest_framework import filters
from rest_framework.generics import ListAPIView


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
        user=authenticate(username=username,password=str(password))
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
        

class feedback(APIView):
    def get(self,request):
        user=feed.objects.all()
        serializer=feedbackserializer(user,many=True)
        return Response({'status':200,'message':serializer.data})
    def post(self,request):
        serializer=feedbackserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':200,'message':'something went wrrong'})
        serializer.save()
        return Response({'status':200,'message':serializer.data})


    

class requst_for_beds(APIView):
    def post(self,request):
        Bed_id=request.data['Bed_id']
        user=beds.objects.get(Bed_id=Bed_id)
        serializer=patientrequestserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':200,'message':serializer.errors})
        serializer.save()
        user.delete()
        return Response({'status':200,'message':'your request is sended to the hospital'})
class filterbeds(ListAPIView):
    queryset=beds.objects.all()
    serializer_class=bedsserializer
    filter_backends=[filters.SearchFilter]
    search_fields=['Hospital_name','Bed_id','Ward_number','Room_number','Bed_type']
class viewhospital(ListAPIView):
    queryset=hospitalinfo.objects.all()
    serializer_class=hospitalinfoserializer
    filter_backends=[filters.SearchFilter]
    search_fields=['hospital_name','hospital_address','hospital_details']

class viewrequest(ListAPIView):
    queryset=patient_info.objects.all()
    serializer_class=patientrequestserializer
    filter_backends=[filters.SearchFilter]
    search_fields=['Hospital_name','Bed_id','Ward_number','Room_number','Disease','Bed_type','patient_name','patient_gender',
                   'patient_age','address','mobile_number','current_medication','allergies','past_surgeries','insurance_policy',
                   'Policy_number','special_request']
@api_view(['get'])
def get_hospital_by_id(request,id):
    user=hospitalinfo.objects.filter(id=id)
    serializer=hospitalinfoserializer(user,many=True)
    return Response({'status':200,'message':serializer.data})

@api_view(['get'])
def view_beds(request,id):
    data=hospitalinfo.objects.get(id=id).hospital_name
    user=beds.objects.filter(Hospital_name=data)
    serializer=bedsserializer(user,many=True)
    return Response({'status':200,'message':serializer.data})


@api_view(['get'])
def rejectrequest(request,id):
        user=patient_info.objects.filter(id=id)
        serializer=patientrequestserializer(user,many=True)
        for data in serializer.data:
              data_serializer=copyserializer(data=data)
              if data_serializer.is_valid():
                     data_serializer.save()
              else:
                     return Response({'status':200,'message':'somthing is wrrong'})
        user.delete()
        return Response({'status':200,'message':'success'})
@api_view(['get'])
def selectrequest(request,id):
        user=patient_info.objects.filter(id=id)
        serializer=patientrequestserializer(user,many=True)
        for data in serializer.data:
              data_serializer=finalinfoserializer(data=data)
              if data_serializer.is_valid():
                     data_serializer.save()
              else:
                     return Response({'status':200,'message':'somthing is wrong'})
        user.delete()
        return Response({'status':200,'message':'success'})




@api_view(['get'])
def discharge(request,id):
     user=finalinformation.objects.filter(id=id)
     serializer=finalinfoserializer(user,many=True)
     for data in serializer.data:
          data_serializer=copyserializer(data=data)
          if data_serializer.is_valid():
                data_serializer.save()
          else:
               return Response({'status':200,'message':'somthing is wrong'})
     user.delete()
     return Response({'status':200,'message':'success'})


@api_view(['get'])
def finalinfo(request):
     user=finalinformation.objects.all()
     serializer=finalinfoserializer(user,many=True)
     return Response({'status':200,'message':serializer.data})


    

    
            
    
    
