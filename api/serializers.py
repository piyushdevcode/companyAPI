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
