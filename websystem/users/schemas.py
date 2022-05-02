from drf_spectacular.extensions import OpenApiAuthenticationExtension
from helpers.jwt_helper import JWTAuthentication


class JWTScheme(OpenApiAuthenticationExtension):
    target_class = JWTAuthentication
    name = "JWT Authentication"

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
