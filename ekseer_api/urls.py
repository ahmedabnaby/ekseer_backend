from django.urls import path, include
from . import views
from knox.views import LogoutView, LogoutAllView


urlpatterns = [
    path('users/', views.UserViewSet.as_view()),
    path('calls/', views.CallViewSet.as_view()),
    path('consultations/', views.ConsultationViewSet.as_view()),
    path('ratings/', views.RatingViewSet.as_view()),

    path('register/', views.CreateUserAPI.as_view()),
    path('create-call/', views.CreateCallAPI.as_view()),
    path('create-consultation/', views.CreateConsultationAPI.as_view()),
    path('create-rating/', views.CreateRatingAPI.as_view()),

    path('update-user/<int:pk>/', views.UpdateUserAPI.as_view()),
    path('update-call/<int:pk>/', views.UpdateCallAPI.as_view()),
    path('update-consultation/<int:pk>/', views.UpdateConsultationAPI.as_view()),
    path('update-rating/<int:pk>/', views.UpdateRatingAPI.as_view()),

    path('login/', views.LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
