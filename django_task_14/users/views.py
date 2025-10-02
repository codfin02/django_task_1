from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LogoutView
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserDetailSerializer, UserLoginSerializer, UserSerializer

User = get_user_model()


class UserSignupView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            login(request, serializer.validated_data['user'])
            return Response({'message': 'login successful.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(LogoutView):
    next_page = None


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    def get_object(self):
        return get_object_or_404(User, id=self.request.user.id)
