from django.shortcuts import render
from rest_framework import generics

from mentoring.serializers import MentorSerializer, ProjectSerializer
from mentoring.models import Mentor, Project, Mentorship


class MentorListView(generics.ListCreateAPIView):
    """Mentor list and create view"""
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorDetailView(generics.RetrieveUpdateAPIView):
    """Mentor detail and update view"""
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class ProjectListView(generics.ListCreateAPIView):
    """Project list and create view"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateAPIView):
    """Project detail and update view"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
