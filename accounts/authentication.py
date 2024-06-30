import logging

from typing import Tuple, TypeVar
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.models import TokenUser
from django.contrib.auth.models import AbstractBaseUser
from core.utils import custom_exceptions as ce
from django.conf import settings

# Get an instance of logger
logger = logging.getLogger('accounts')

AuthUser = TypeVar("AuthUser", AbstractBaseUser, TokenUser)

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request: Request) -> Tuple[AuthUser, Token] | None:
        try:
            header = self.get_header(request)
            raw_token = None

            if header is None:
                raw_token = request.COOKIES.get(settings.AUTH_COOKIE)
            else:
                raw_token = self.get_raw_token(header)
            
            if raw_token is None:
                return None

            validated_token = self.get_validated_token(raw_token)

            return self.get_user(validated_token), validated_token
        except Exception as e:
            logger.error(f'CUSTOM AUTHENTICATION: {e}')
            raise ce.InternalServerError