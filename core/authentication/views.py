from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import generics,status, serializers
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer
from .mesagges.responses_ok import LOGIN_OK 
from .mesagges.responses_error import LOGIN_CREDENTIALS_REQUIRED_ERROR, LOGIN_CREDENTIALS_ERROR

# Create your views here.   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class LoginView(generics.GenericAPIView):
    def get(self, request):
        data_response = {"msg": "Metodo GET no permitido"}
        return Response(data_response, status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        if email is None or password is None:
            return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_400_BAD_REQUEST)

        else:
            user: authenticate(email = email, password = password)
            if user is not None:
               return Response({
               "user": UserSerializer(user, context = self.get_serializer_context()).data,
               "message": "Sesión iniciada correctamente"})
            else: 
                return Response(LOGIN_CREDENTIALS_ERROR, status=status.HTTP_401_UNAUTHORIZED)

class SignUpView(generics.GenericAPIView):
    
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user":UserSerializer(user, context = self.get_serializer_context()).data,
                "message": "Usuario creado con éxito. Ahora puedes iniciar sesión"
            },
        ) 

        pass

