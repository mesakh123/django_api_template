import jwt
from django.conf import settings
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from users.models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print("Authenticate")
        auth_header = get_authorization_header(request)

        auth_data = auth_header.decode("utf-8")

        auth_token = auth_data.split(" ")
        if len(auth_token) != 2:
            raise exceptions.AuthenticationFailed({"message": "Token not valid"})

        token = auth_token[1]

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
            username = payload.get("username", None)
            email = payload.get("email", None)

            if username:
                user = User.objects.get(username=username)
            elif email:
                email = User.objects.get(email=email)
            return (user, token)

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Token is expired, login again")

        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed("Token is invalid,")

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")

        return super().authenticate(request)
