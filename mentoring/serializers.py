from rest_framework.serializers import ModelSerializer, SerializerMethodField
from mentoring.models import Mentor, Project, Mentorship


class MentorSerializer(ModelSerializer):
    """A serializer for the Mentor model"""
    class Meta:
        model = Mentor
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    """A serializer for the Project model with its Mentors"""
    mentors = SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'

    @staticmethod
    def __get_project_obj(obj) -> Project:
        if type(obj) is dict:
            return Project.objects.get(id=obj.get('id'))
        elif type(obj) is Project:
            return obj

    def get_mentors(self, obj) -> MentorSerializer(many=True):
        mentors = self.__get_project_obj(obj).get_mentors()
        return MentorSerializer(mentors, many=True).data
    
class MentorshipSerializer(ModelSerializer):
    """A serializer for the Mentorship model"""
    class Meta:
        model = Mentorship
        fields = '__all__'
