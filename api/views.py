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

    def get_queryset(self):
        """
        Option to search by company name if query parameter in URL
        """
        queryset = Company.objects.all()
        company_name = self.request.query_params.get('name')

        # query param provided in path
        if company_name:
            queryset = queryset.filter(name=company_name)
        return queryset

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        company_id = self.request.query_params.get('cid')
        print('company ID: ',company_id)
        if company_id:
            print('jinga')
            return Response({"error":"Invalid Company ID in query parameters"},status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        print('self: ',self)
        print('serializer',serializer)
        company_obj = Company.objects.get(pk=self.kwargs['cid'])
        company_id = self.request.query_params.get('cid')
        print('company ID: ',company_id)
        # serializer.save(company_id=company_obj)
