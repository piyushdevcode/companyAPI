from math import perm
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets,permissions
from api.models import Company,Team
from . import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
@api_view()
def api_root(request):
    """
    Root of API
    """
    return Response({'ok':200},status=status.HTTP_200_OK)

#/ For sake of refactoring have used the ModelViewSet

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        print('args',args)
        print('kwargs',kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        print('self: ',self)
        print('serializer',serializer)
        company_obj = Company.objects.get(pk=self.kwargs['id'])
        serializer.save(company_id=company_obj)
