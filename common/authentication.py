from rest_framework.permissions import IsAuthenticated


class AuthenticationMixin:
    permission_classes = (IsAuthenticated,)
