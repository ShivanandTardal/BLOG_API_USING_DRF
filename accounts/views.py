from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,generics
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class=UserSerializer
    permission_classes=[]

    def post(self,request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"Post created successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
class LoginView(APIView):
    permission_classes=[]
    def post(self,request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens=create_jwt_pair_for_user(user)

            response = {
                "message":"Login successful",
                "token": tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)
        
        else:
            response = {
                "message":"Login failed"
            }
            return Response(data=response, status=status.HTTP_200_OK)
    def get(self,request:Request):
        content={
            "user":str(request.user),
            "auth":str(request.auth)
        }
        return Response(data=content,status=status.HTTP_200_OK)