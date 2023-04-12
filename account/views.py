from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import AccountSerializer, LoginSerilizer, CreateAccountSerializer, ChangePasswordSerializer


class RegisterView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = CreateAccountSerializer


class AccountView(generics.RetrieveUpdateAPIView):

    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerilizer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        type_user = "admin" if user.is_superuser else "senator"

        response = {
            "token": str(token),
            "type": type_user
        }

        return Response(response, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get_object(self):

        return Token.objects.get(user=self.request.user)

    def post(self, request):
        token = self.get_object()
        token.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePasswordView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def put(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        user.set_password(serializer.validated_data["new_password"])
        user.save()

        token, _ = Token.objects.get_or_create(user=user)
        token.delete()

        return Response({"message": "Password Updated"}, status=status.HTTP_200_OK)
