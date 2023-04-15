from django.urls import path
from mentoring import views


urlpatterns = [
    # Mentor model views
    path('mentor', views.MentorListView.as_view()),
    path('mentor/<int:pk>/', views.MentorDetailView.as_view()),
]