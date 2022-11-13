# cookieapp/authenticate.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import HTTP_HEADER_ENCODING, authentication
from django.contrib.auth import get_user_model
from django.conf import settings

from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions

def enforce_csrf(request):
    # def dummy_get_response(request):  # pragma: no cover
    #         return None

    # check = CSRFCheck(dummy_get_response)

    check = CSRFCheck()
    check.process_request(request)
    reason = check.process_view(request, None, (), {})
    if reason:
        raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)

# class CustomAuthentication(JWTAuthentication):
    
#     def authenticate(self, request):
#         header = self.get_header(request)
        
#         if header is None:
#             if settings.SIMPLE_JWT['AUTH_COOKIE'] in request.COOKIES:
#                 raw_token = request.COOKIES['access_token']
#             print('raw token in authetication', raw_token)
#         else:
#             raw_token = self.get_raw_token(header)
#         if raw_token is None:
#             return None

#         validated_token = self.get_validated_token(raw_token)
#         enforce_csrf(request)
#         return self.get_user(validated_token), validated_token



class JWTAuth(JWTAuthentication):
    """
    An authentication plugin that authenticates requests through a JSON web
    token provided in a request header.
    """

    www_authenticate_realm = "api"
    media_type = "application/json"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_model = get_user_model()

    def authenticate(self, request):
        cookie = request.COOKIES.get("access_token")
        raw_token = cookie.encode(HTTP_HEADER_ENCODING)
        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token