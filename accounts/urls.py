from django.urls import path
from .views import CustomLoginView, CustomLogoutView, SignupView, UserCreateAPIView
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
]

urlpatterns += [
    path('api/v1/token/', ObtainAuthToken.as_view(), name='api_token'),
    path('api/v1/signup/', UserCreateAPIView.as_view(), name='create_user'),
]

