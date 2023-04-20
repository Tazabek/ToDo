from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

num_codes = {
    "0999" : "Мегаком: ",
    "0998" : "Мегаком: ",
    "0997" : "Мегаком: ",
    "0995" : "Мегаком: ",
    "0990" : "Мегаком: ",
    "0755" : "Мегаком: ",
    "0550" : "Мегаком: ",
    "0551" : "Мегаком: ",
    "0552" : "Мегаком: ",
    "0553" : "Мегаком: ",
    "0554" : "Мегаком: ",
    "0555" : "Мегаком: ",
    "0556" : "Мегаком: ",
    "0557" : "Мегаком: ",
    "0558" : "Мегаком: ",
    "0559" : "Мегаком: ",
    "0770" : "Билайн: ",
    "0771" : "Билайн: ",
    "0772" : "Билайн: ",
    "0773" : "Билайн: ",
    "0774" : "Билайн: ",
    "0775" : "Билайн: ",
    "0776" : "Билайн: ",
    "0777" : "Билайн: ",
    "0778" : "Билайн: ",
    "0779" : "Билайн: ",
    "0220" : "Билайн: ",
    "0221" : "Билайн: ",
    "0222" : "Билайн: ",
    "0223" : "Билайн: ",
    "0224" : "Билайн: ",
    "0225" : "Билайн: ",
    "0227" : "Билайн: ",
    "0500" : "О! :",
    "0501" : "О! :",
    "0502" : "О! :",
    "0503" : "О! :",
    "0504" : "О! :",
    "0505" : "О! :",
    "0507" : "О! :",
    "0508" : "О! :",
    "0509" : "О! :",
    "0700" : "О! :",
    "0701" : "О! :",
    "0703" : "О! :",
    "0704" : "О! :",
    "0705" : "О! :",
    "0706" : "О! :",
    "0707" : "О! :",
    "0708" : "О! :",
    "0709" : "О! :",
}


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only= True)

    class Meta:
        model = User
        fields = (
            'id', 
            'username',
            'email',
            'phone_number',
            'created_at',
            'age',
            'password',
            'confirm_password'
        )

    def create(self, validated_data):
        if not validated_data['confirm_password']:
            raise serializers.ValidationError('Confirm your password')
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError('passwords are not same!')
        for i in num_codes:
            if validated_data['phone_number'].startswith(i):
                user = User(
                username = validated_data['username'],
                email = validated_data['email'],
                phone_number = validated_data['phone_number'],
                created_at = validated_data['created_at'],
                age = validated_data['age']
                )
                user.set_password(validated_data['password'])
                user.save()
                return user
        else:
            raise serializers.ValidationError('phone number is not correct!')
        

class UpdateUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only= True)

    class Meta:
        model = User
        fields = (
            'id', 
            'username',
            'email',
            'phone_number',
            'password',
            'confirm_password'
        )

    
    def update(self, instance, validated_data):
        if not validated_data['confirm_password']:
            raise serializers.ValidationError('Confirm your password')
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError('passwords are not same!')
        for i in num_codes:
            if validated_data['phone_number'].startswith(i):
                instance.set_password(validated_data['password'])
                instance.username = validated_data['username']
                instance.email = validated_data['email']
                instance.phone_number = validated_data['phone_number']
                instance.save()
                return instance
        else:
            raise serializers.ValidationError('phone number is not correct!')