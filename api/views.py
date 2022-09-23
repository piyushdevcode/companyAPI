from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.reverse import reverse
from api.models import Company, Team
from . import serializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.permissions import IsSuperAdmin


@api_view()
def api_root(request, format=None):
    """
    Root of API
    """
    return Response(
        {
            "company": reverse("company-list", request=request, format=format),
            "team": reverse("team-list", request=request, format=format),
            "listallteams": reverse("all-teams-list", request=request, format=format),
        }
    )


# / For sake of refactoring have used the ModelViewSet


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [IsSuperAdmin]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """
        Option to search by company name if query parameter in URL
        """
        queryset = Company.objects.all()
        company_name = self.request.query_params.get("name")
        # query param provided in path
        if company_name:
            queryset = queryset.filter(name=company_name)
        return queryset


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = [IsSuperAdmin]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        print("self: ", self)
        print("serializer", serializer)
        company_obj = Company.objects.get(pk=self.kwargs["cid"])
        company_id = self.request.query_params.get("cid")
        print("company ID: ", company_id)
        serializer.save(company_id=company_obj)


class ListAllTeamsViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.prefetch_related("teams")
    serializer_class = serializers.AllTeamSerializer
    lookup_url_kwarg = "id"
    permission_classes = [IsSuperAdmin]
