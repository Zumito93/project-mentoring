import json
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.urls import reverse
from django.contrib.auth.models import AnonymousUser
from mentoring.models import Mentor, Project, Mentorship
from mentoring.views import MentorListView, MentorDetailView, ProjectListView, ProjectDetailView, MentorshipListView, MentorshipDetailView
from mentoring.serializers import MentorSerializer, ProjectSerializer, MentorshipSerializer
from mentoring.utils import Gender


class MentoringGetAPITestCase(APITestCase):
    """Test Mentoring API GET requests"""

    def setUp(self):
        self.factory = APIRequestFactory()

        # Mentor model records
        self.mentor_px = Mentor.objects.create(email='professor_xavier@mail.com',
                                          name='Professor X',
                                          gender=Gender.MALE)
        self.mentor_mc = Mentor.objects.create(email='marie_curie@mail.com',
                                          name='Marie Curie',
                                          gender=Gender.FEMALE)
        self.mentor_pm = Mentor.objects.create(email='professor_mosby@mail.com',
                                          name='Ted Mosby',
                                          gender=Gender.MALE)
        self.mentor_mx = Mentor.objects.create(email='mr_x@mail.com',
                                          name='Mr. X',
                                          gender=Gender.OTHER)

        # Project model records
        self.project_a = Project.objects.create(name='Project Alpha')
        self.project_b = Project.objects.create(name='Project Beta')
        self.project_g = Project.objects.create(name='Project Gamma')
        self.project_d = Project.objects.create(name='Project Delta')

        # Mentorship model records
        self.mentorship_1 = Mentorship.objects.create(mentor=self.mentor_px, project=self.project_a)
        Mentorship.objects.create(mentor=self.mentor_px, project=self.project_b)
        Mentorship.objects.create(mentor=self.mentor_px, project=self.project_g)
        Mentorship.objects.create(mentor=self.mentor_px, project=self.project_d)
        Mentorship.objects.create(mentor=self.mentor_mc, project=self.project_g)
        Mentorship.objects.create(mentor=self.mentor_mx, project=self.project_g)
        Mentorship.objects.create(mentor=self.mentor_mx, project=self.project_d)

    # Test get list requests
    # TODO: paginate objects or return data not paginated from view
    def test_get_mentor_list(self):
        # get API response
        request = self.factory.get(reverse('MentorListView'))
        force_authenticate(request, user=AnonymousUser)
        response = MentorListView.as_view()(request)
        # get data from db
        mentors = Mentor.objects.all()
        serializer = MentorSerializer(mentors, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project_list(self):
        # get API response
        request = self.factory.get(reverse('ProjectListView'))
        force_authenticate(request, user=AnonymousUser)
        response = ProjectListView.as_view()(request)
        # get data from db
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_mentorship_list(self):
        # get API response
        request = self.factory.get(reverse('MentorshipListView'))
        force_authenticate(request, user=AnonymousUser)
        response = MentorshipListView.as_view()(request)
        # get data from db
        mentorships = Mentorship.objects.all()
        serializer = MentorshipSerializer(mentorships, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test model get requests
    def test_get_mentor(self):
        mentor = self.mentor_px
        # get API response
        request = self.factory.get(reverse('MentorDetailView', kwargs={'pk': 0}))
        force_authenticate(request, user=AnonymousUser)
        response = MentorDetailView.as_view()(request, pk=mentor.id)
        serializer = MentorSerializer(mentor)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project(self):
        project = self.project_a
        # get API response
        request = self.factory.get(reverse('ProjectDetailView', kwargs={'pk': 0}))
        force_authenticate(request, user=AnonymousUser)
        response = ProjectDetailView.as_view()(request, pk=project.id)
        serializer = ProjectSerializer(project)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_mentorship(self):
        mentorship = self.mentorship_1
        # get API response
        request = self.factory.get(reverse('MentorshipDetailView', kwargs={'pk': 0}))
        force_authenticate(request, user=AnonymousUser)
        response = MentorshipDetailView.as_view()(request, pk=mentorship.id)
        serializer = MentorshipSerializer(mentorship)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MentoringPostAPITestCase(APITestCase):
    """Test Mentoring API POST requests"""

    def setUp(self):
        self.factory = APIRequestFactory()

        self.valid_mentor_payload = {
            'email': 'professor_xavier@mail.com',
            'name': 'Professor X',
            'gender': 'M'
        }
        self.invalid_mentor_payload = {
            'email': 'professor_xavier%mail.com',
            'name': 'Professor X',
            'gender': '1'
        }

    def test_create_valid_mentor(self):
        request = self.factory.post(
            reverse('MentorListView'),
            data=json.dumps(self.valid_mentor_payload),
            content_type='application/json'
        )
        force_authenticate(request, user=AnonymousUser)
        response = MentorListView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_mentor(self):
        request = self.factory.post(
            reverse('MentorListView'),
            data=json.dumps(self.invalid_mentor_payload),
            content_type='application/json'
        )
        force_authenticate(request, user=AnonymousUser)
        response = MentorListView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
