from rest_framework import serializers
from .models import StudyItem

# Serialize to represent study information in JSON format
class StudyItemSerializer(serializers.ModelSerializer):
    nct_id = serializers.CharField(max_length=30)
    study_url = serializers.CharField(max_length=300)
    study_title = serializers.CharField(max_length=500)
    study_status = serializers.CharField(max_length=50)
    sponsor_collaborators = serializers.CharField(max_length=500)

    class Meta:
        model = StudyItem
        fields = ('__all__')