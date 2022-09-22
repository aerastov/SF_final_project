from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import requests
from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
# from api.mixins import ApiErrorsMixin, ApiAuthMixin, PublicApiMixin
# from users.services import user_get_or_create
# from users.selectors import user_get_me

GOOGLE_ACCESS_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'

def google_validate_access_token(*, access_token: str) -> bool:
    response = requests.get(GOOGLE_ACCESS_TOKEN_INFO_URL, params={'access_token': access_token})
    if not response.ok:
        return False
        # raise ValidationError('access_token is invalid.')
    audience = response.json()['aud']
    print('audience', audience)
    # if audience != settings.GOOGLE_OAUTH2_CLIENT_ID:
    #     raise ValidationError('Invalid audience.')
    return True


def google_get_user_info(*, access_token: str) -> bool:
    response = json.loads(requests.get(GOOGLE_USER_INFO_URL, params={'access_token': access_token}).content.decode('UTF-8'))
    print('response.content2', response)
    # print('response.content', response.content.decode('UTF-8'))
    email = response.get('email', None)
    first_name = response['given_name', None]
    last_name = response['given_name', None]
    avatar = response['picture', None]
    # После доработки Страницы регистрации на react, доработать регистрацию юзера в модели
    return True



@api_view(['POST'])
def user_init(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        access_token = request.META.get('HTTP_AUTHORIZATION', None)
        if google_validate_access_token(access_token=access_token) is True:
            google_get_user_info(access_token=access_token)
        else:
            return Response(data={'status': 'access_token is invalid'}, status=403)
        print("access_token: ", access_token)
        print("data: ", data)
        return Response(data={'status': 'ok'}, status=200)
        # return JsonResponse(access_token)




