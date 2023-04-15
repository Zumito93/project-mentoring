from rest_framework.serializers import ModelSerializer
from mentoring.models import Mentor, Project, Mentorship


class MentorSerializer(ModelSerializer):
    """A serializer for the Mentor model"""
    class Meta:
        model = Mentor
        fields = '__all__'
