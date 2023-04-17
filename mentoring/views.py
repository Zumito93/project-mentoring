from django.shortcuts import render
from rest_framework import generics
from drf_spectacular.utils import extend_schema

from mentoring.serializers import MentorSerializer, ProjectSerializer, MentorshipSerializer
from mentoring.models import Mentor, Project, Mentorship


# Mentor views
class MentorListView(generics.ListCreateAPIView):
    """Mentor list and create view"""
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

    # GET Mentors
    @extend_schema(
        operation_id="getMentors",
        summary="Retrieve all mentors.",
        description="Returns a list of all mentors."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # POST Mentor
    @extend_schema(
        operation_id="createMentor",
        summary="Create a mentor.",
        description="Creates a mentor."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class MentorDetailView(generics.RetrieveUpdateAPIView):
    """Mentor detail and update view"""
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

    # GET Mentor
    @extend_schema(
        operation_id="getMentor",
        summary="Retrieve a mentor by id.",
        description="Returns the mentor for the queried id."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    # PUT Mentor
    @extend_schema(
        operation_id="putMentor",
        summary="Update a mentor by id.",
        description="Updates mentor data for the path id."
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    # PATCH Mentor
    @extend_schema(
        operation_id="patchMentor",
        summary="Update a mentor by id.",
        description="Updates mentor data for the path id."
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


# Project views
class ProjectListView(generics.ListCreateAPIView):
    """Project list and create view"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # GET Projects
    @extend_schema(
        operation_id="getProjects",
        summary="Retrieve all projects.",
        description="Returns a list of all projects with their mentors."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # POST Project
    @extend_schema(
        operation_id="createProject",
        summary="Create a project.",
        description="Creates a project."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ProjectDetailView(generics.RetrieveUpdateAPIView):
    """Project detail and update view"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # GET Project
    @extend_schema(
        operation_id="getProject",
        summary="Retrieve a project by id.",
        description="Returns the project with its mentors for the queried id."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    # PUT Project
    @extend_schema(
        operation_id="putProject",
        summary="Update a project by id.",
        description="Updates project data for the path id."
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    # PATCH Project
    @extend_schema(
        operation_id="patchProject",
        summary="Update a project by id.",
        description="Updates project data for the path id."
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

# Mentorship views
class MentorshipListView(generics.ListCreateAPIView):
    """Mentorship list and create view"""
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer

    # GET Mentorships
    @extend_schema(
        operation_id="getMentorships",
        summary="Retrieve all mentorships.",
        description="Returns a list of all mentorships."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # POST Mentorships
    @extend_schema(
        operation_id="createMentorship",
        summary="Create a mentorship.",
        description="Creates a mentorship by relating a mentor with a project."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class MentorshipDetailView(generics.RetrieveUpdateAPIView):
    """Mentorship detail and update view"""
    queryset = Mentorship.objects.all()
    serializer_class = MentorshipSerializer

    # GET Mentorship
    @extend_schema(
        operation_id="getMentorship",
        summary="Retrieve a mentorship by id.",
        description="Returns the mentorship for the queried id."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    # PUT Mentorship
    @extend_schema(
        operation_id="putMentorship",
        summary="Update a mentorship by id.",
        description="Updates mentorship data for the path id."
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    # PATCH Mentorship
    @extend_schema(
        operation_id="patchMentorship",
        summary="Update a mentorship by id.",
        description="Updates mentorship data for the path id."
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
