from rest_framework import serializers
from api.models import Company,Team

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    # company_id = serializers.HyperlinkedRelatedField(view_name='company-detail',read_only=True)
    class Meta:
        model = Team
        fields = '__all__'
        # We are getting the company_id from URL so no need of it in JSON when creating team
        extra_kwargs = {'company_id':{'read_only':True}}

class AllTeamSerializer(serializers.ModelSerializer):
    # teams = serializers.HyperlinkedRelatedField(many=True,view_name='team-detail',read_only=True,lookup_url_kwarg='id')
    teams = serializers.PrimaryKeyRelatedField(many=True,read_only=True,
    pk_field=serializers.UUIDField(format='hex')
    )
    class Meta:
        model = Company
        fields = ['name','teams']