from django.db import models
from django.contrib.auth.models import User
gen=(('Male','Male'),
     ('Female','Female'),
     ('Other','Other'))
sta=(('Andhra Pradesh','Andhra Pradesh'),
     ('Arunachal Pradesh','Arunachal Pradesh'),
     ('Assam','Assam'),
     ('Bihar','Bihar'),
     ('Chhattisgarh','Chhattisgarh'),
     ('Goa','Goa'),
     ('Gujarat','Gujarat'),
     ('Haryana','Haryana'),
     ('Himachal Pradesh','Himachal Pradesh'),
     ('Jharkhand','Jharkhand'),
     ('Karnataka','Karnataka'),
     ('Kerala','Kerala'),
     ('Madhya Pradesh','Madhya Pradesh'),
     ('Maharashtra','Maharashtra'),
     ('Manipur','Manipur'),
     ('Meghalaya','Meghalaya'),
     ('Mizoram','Mizoram'),
     ('Nagaland','Nagaland'),
     ('Odisha','Odisha'),
     ('Punjab','Punjab'),
     ('Rajasthan','Rajasthan'),
     ('Sikkim','Sikkim'),
     ('Tamil Nadu','Tamil Nadu'),
     ('Telangana','Telangana'),
     ('Tripura','Tripura'),
     ('Uttar Pradesh','Uttar Pradesh'),
     ('Uttarakhand','Uttarakhand'),
     ('West Bengal','West Bengal'),
     ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
     ('Chandigarh','Chandigarh'),
     (' Dadra and Nagar Haveli and Daman and Diu',' Dadra and Nagar Haveli and Daman and Diu'),
     ('Lakshadweep','Lakshadweep'),
     ('Delhi','Delhi'),
     ('Puducherry','Puducherry')
    )
status=(('Married','Married'),
        ('Unmarried','Unmarried'))
class registration(models.Model):
    User=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    full_name=models.CharField(max_length=200)
    fathers_name=models.CharField(max_length=200)
    gender=models.CharField(choices=gen,max_length=200)
    email=models.CharField(max_length=200,unique=True)
    code=models.TextField()
    address1=models.TextField()
    address2=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(choices=sta,max_length=50)
    zip=models.IntegerField()
    def __str__(self):
        return self.full_name

