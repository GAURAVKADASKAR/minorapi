from home.models import *
from rest_framework import serializers



class registerserializer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields="__all__"
    def create(self, validated_data):
        username=validated_data['email']
        user=User.objects.filter(username=username)
        if user.exists():
            raise serializers.ValidationError({'error':'username is already taken'})
        obj1=registration.objects.create(
            full_name=validated_data['full_name'],
            fathers_name=validated_data['fathers_name'],
            gender=validated_data['gender'],
            email=validated_data['email'],
            code=validated_data['code'],
            address1=validated_data['address1'],
            address2=validated_data['address2'],
            city=validated_data['city'],
            state=validated_data['state'],
            zip=validated_data['zip']
        )
        obj1.save()
        obj2=User.objects.create(
            username=validated_data['email']
        )
        obj2.set_password(validated_data['code'])
        obj2.save()
        return validated_data

class loginserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
    
class profileserializer(serializers.ModelSerializer):
    class Meta:
        model=registration
        fields="__all__"
        