from django.urls import path
from mentoring import views


urlpatterns = [
    # Mentor model views
    path('mentors', views.MentorListView.as_view(), name='MentorListView'),
    path('mentors/<int:pk>', views.MentorDetailView.as_view(), name='MentorDetailView'),
    # Project model views
    path('projects', views.ProjectListView.as_view(), name='ProjectListView'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='ProjectDetailView'),
    # Mentorship model views
    path('mentorships', views.MentorshipListView.as_view(), name='MentorshipListView'),
    path('mentorships/<int:pk>', views.MentorshipDetailView.as_view(), name='MentorshipDetailView'),
]
