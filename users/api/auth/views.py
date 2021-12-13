from rest_framework_simplejwt.views import TokenObtainPairView

from users.api.auth.serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
