from django.shortcuts import render
from rest_framework import generics

from mentoring.serializers import MentorSerializer
from mentoring.models import Mentor, Project, Mentorship


class MentorListView(generics.ListCreateAPIView):
    """Mentor list and create view"""
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorDetailView(generics.RetrieveUpdateAPIView):
    """Mentor detail and update view"""
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer