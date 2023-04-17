from django.urls import path
from mentoring import views


urlpatterns = [
    # Mentor model views
    path('mentor', views.MentorListView.as_view(), name='MentorListView'),
    path('mentor/<int:pk>', views.MentorDetailView.as_view(), name='MentorDetailView'),
    # Project model views
    path('project', views.ProjectListView.as_view(), name='ProjectListView'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='ProjectDetailView'),
    # Mentorship model views
    path('mentorship', views.MentorshipListView.as_view(), name='MentorshipListView'),
    path('mentorship/<int:pk>', views.MentorshipDetailView.as_view(), name='MentorshipDetailView'),
]
