from rest_framework import serializers
from api.models import Company, Team


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

        # We are getting the company_id from URL so no need of it when creating team
        extra_kwargs = {"company_id": {"read_only": True}}


class AllTeamSerializer(serializers.ModelSerializer):
    """
    serializer for listing all companies with their teams
    """

    teams = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ["name", "teams"]
