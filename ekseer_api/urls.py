from django.urls import path, include
from . import views
from knox.views import LogoutView, LogoutAllView


urlpatterns = [
    path('users/', views.UserViewSet.as_view()),
    path('calls/', views.CallViewSet.as_view()),
    # path('doctors/', views.DoctorViewSet.as_view()),
    path('register/', views.CreateUserAPI.as_view()),
    path('create-call/', views.CreateCallAPI.as_view()),
    # path('doctor-register/', views.CreateDoctorAPI.as_view()),
    path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
    path('update-call/<int:pk>/', views.UpdateCallAPI.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('login/', views.LoginAPIView.as_view()),
    # path('doctor-login/',  views.DoctorLoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
]
