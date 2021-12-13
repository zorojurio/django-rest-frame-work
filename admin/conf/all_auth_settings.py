# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]
#

"""
override the serializer that is used by the social login authentication
JWT_TOKEN_CLAIMS_SERIALIZER - A custom JWT Claim serializer.
Default is rest_framework_simplejwt.serializers.TokenObtainPairSerializer
see moore at https://dj-rest-auth.readthedocs.io/en/latest/configuration.html

"""
REST_AUTH_SERIALIZERS = {
    'JWT_TOKEN_CLAIMS_SERIALIZER': 'users.api.auth.serializers.MyTokenObtainPairSerializer'
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': 'client_id',
            'secret': 'secret_id',
            'key': ''
        }
    },
    'facebook': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': 'client_id',
            'secret': 'secret_id',
            'key': ''
        }
    },
    'linkedin': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'SCOPE': [
            'r_emailaddress',
            'r_basicprofile',
            'w_member_social'
        ],
        'APP': {
            'client_id': 'client_id',
            'secret': 'secret_id',
            'key': ''
        }
    },
}
