from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', obtain_auth_token, name='login_token'),
]
