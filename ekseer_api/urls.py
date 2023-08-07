from django.urls import path
from . import views
from knox.views import LogoutView, LogoutAllView


urlpatterns = [
    path('users/', views.UserViewSet.as_view()),
    # path('doctors/', views.DoctorViewSet.as_view()),
    path('register/', views.CreateUserAPI.as_view()),
    # path('doctor-register/', views.CreateDoctorAPI.as_view()),
    path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    # path('doctor-login/',  views.DoctorLoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
]
