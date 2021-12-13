import datetime

from django.conf import settings as main_settings
from django.utils import timezone
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

expire_delta = main_settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']


# sending additional data along with the token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        """
        data['chanuka'] = 'hello hacker,' will be encoded in the token
        :param user:
        :return:
        """
        data = super().get_token(user)
        data['name'] = user.username
        data['chanuka'] = 'hello hacker,'
        if user.is_superuser:
            data['role'] = 'Admin'
        else:
            pass
            # if user.role:
            #     data['role'] = user.role.name
        print(user)
        return data

    def validate(self, *args, **kwargs):
        """
        after a successfull login
        "refresh": "token
        "access": "token
        "name": "admin",
        "expires": "2021-12-13T14:14:00.507552Z"
        :param args:
        :param kwargs:
        :return:
        """
        data = super().validate(*args, **kwargs)
        data['name'] = self.user.username
        data['expires'] = timezone.now() + expire_delta - datetime.timedelta(seconds=200)
        return data

    def create(*args, **kwargs):
        return super().update(*args, **kwargs)

    def update(self, *args, **kwargs):
        return super().update(*args, **kwargs)
