from rest_framework import authentication, serializers, views
from .models import CustomUser, Call
from django.core.validators import RegexValidator
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(format='%m-%d-%Y')
    class Meta:
        model = CustomUser
        fields = '__all__'

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'required': True}
        }

    def validate(self, attrs):
        email = attrs.get('email', '').strip().lower()
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email id already exists.')
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'full_name',
            'mobile_number', 
            'email', 
        ]
        extra_kwargs = {
            'password': {'write_only':True}
        }


    def update(self, instance, validated_data):
        # password = validated_data.pop('password')
        # if password:
        #     instance.set_password(password)
        instance = super().update(instance, validated_data)
        return instance


class LoginSerializer(serializers.Serializer):
    iqama_number = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)


    def validate(self, attrs):
        iqama_number = attrs.get('iqama_number')
        password = attrs.get('password')

        if not iqama_number or not password:
            raise serializers.ValidationError("Please give both iqama_number and password.")

        if not CustomUser.objects.filter(iqama_number=iqama_number).exists():
            raise serializers.ValidationError('Iqama Number/ID not exist.')

        user = authenticate(request=self.context.get('request'), iqama_number=iqama_number,
                            password=password)
        print(user, "AAAAAAAARGH")
        if not user:
            raise serializers.ValidationError("Wrong Credentials.")

        attrs['user'] = user
        return attrs

class CreateCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'

    def validate(self, attrs):
        meeting_id = attrs.get('meeting_id', '').strip().lower()
        if Call.objects.filter(meeting_id=meeting_id).exists():
            raise serializers.ValidationError('Meeting id already exists.')
        return attrs

    def create_call(self, meeting_id, patient_id,doctor_id, **extra_fields):
        if not meeting_id:
            raise ValueError("The meeting_id is not given.")
        call = self.model(meeting_id=meeting_id,patient_id=patient_id, doctor_id=doctor_id,is_new=True, **extra_fields)
        call.save()
        return call
    
class UpdateCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'


    def update(self, instance, validated_data):
        # password = validated_data.pop('password')
        # if password:
        #     instance.set_password(password)
        instance = super().update(instance, validated_data)
        return instance

