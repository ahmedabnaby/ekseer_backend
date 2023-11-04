from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, Call, Consultation, Rating
from .serializers import CreateRatingSerializer, CreateUserSerializer, UpdateUserSerializer, LoginSerializer, UserSerializer, CreateCallSerializer, UpdateCallSerializer, CreateConsultationSerializer, UpdateConsultationSerializer
from knox import views as knox_views
from django.contrib.auth import login


class CreateUserAPI(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)

class CreateCallAPI(CreateAPIView):
    queryset = Call.objects.all()
    serializer_class = CreateCallSerializer
    permission_classes = (AllowAny,)

class CreateConsultationAPI(CreateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = CreateConsultationSerializer
    permission_classes = (AllowAny,)

class UserViewSet(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_all_users(self, request):
        users = self.queryset.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

class CallViewSet(ListAPIView):
    queryset = Call.objects.all()
    serializer_class = CreateCallSerializer

    def get_all_calls(self, request):
        calls = self.queryset.all()
        serializer = self.serializer_class(calls, many=True)
        return Response(serializer.data)
    
class ConsultationViewSet(ListAPIView):
    queryset = Consultation.objects.all()
    serializer_class = CreateConsultationSerializer

    def get_all_consultations(self, request):
        consultations = self.queryset.all()
        serializer = self.serializer_class(consultations, many=True)
        return Response(serializer.data)


class UpdateUserAPI(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer

class UpdateCallAPI(UpdateAPIView):
    queryset = Call.objects.all()
    serializer_class = UpdateCallSerializer

class UpdateConsultationAPI(UpdateAPIView):
    queryset = Consultation.objects.all()
    serializer_class = UpdateConsultationSerializer

class LoginAPIView(knox_views.LoginView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response.data, status=status.HTTP_200_OK)

class CreateRatingAPI(CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializer
    permission_classes = (AllowAny,)

class RatingViewSet(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = CreateRatingSerializer

    def get_all_ratings(self, request):
        ratings = self.queryset.all()
        serializer = self.serializer_class(ratings, many=True)
        return Response(serializer.data)