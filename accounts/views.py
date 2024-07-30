from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import AccountSerializer

class AccountCreateAPIView(APIView) :
    def post(self,request) :
        serializer = AccountSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True) :
            user = serializer.save()
            roles = []
            if user.is_superuser:
                roles.append({"role" : "ADMIN"})
            if user.is_staff:
                roles.append({"role" : "STAFF"})
            if not user.is_superuser and not user.is_staff:
                roles.append({"role": "USER"})
            
            return Response({
                "username" : user.username,
                "nickname": user.nickname,
                "roles": roles
                }, status=201)
                