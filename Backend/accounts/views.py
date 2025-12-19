from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import (
    UserCreateSerializer,
    UserListSerializer,
    MeSerializer,
)
from .permissions import IsAdmin


# 👤 Logged-in user details
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = MeSerializer(request.user)
        return Response(serializer.data)


# 👥 Admin creates users
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


# 📋 Admin list all users
class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


# ✏ Admin update user
class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


# ❌ Admin deactivate user
class DeactivateUserView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return Response({"message": "User deactivated"})
