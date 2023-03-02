from django.contrib.auth.models import User
from .serializers import TokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class LoginTokenAPI(TokenObtainPairView):
    serializer_class = TokenSerializer
