from django.urls import path

from users.api.social.views import FacebookLogin

app_name = 'social'
urlpatterns = [
    path('facebook/', FacebookLogin.as_view(), name='fb_login')
]
