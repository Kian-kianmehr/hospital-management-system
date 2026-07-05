from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import PatientProfileSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterAPIView(CreateAPIView):

    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "message": "User registered successfully."
            },
            status=status.HTTP_201_CREATED
        )
    

class PatientProfileAPIView(RetrieveUpdateAPIView):

    serializer_class = PatientProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.patient_profile
    



class LoginAPIView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_200_OK
        )