from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Mentor(models.Model):
    """A model that represents a mentor"""
    email = models.EmailField()
    name = models.CharField(max_length=128)
    from mentoring.utils import Gender
    gender = models.CharField(max_length=8, choices=Gender.choices)


class Project(models.Model):
    """A model that represents a project"""
    name = models.CharField(max_length=128)

    def get_mentors(self) -> list[Mentor]:
        project_mentorships = Mentorship.objects.filter(project=self)
        mentors = []
        for mentorship in project_mentorships:
            mentors.append(mentorship.mentor)
        return mentors


class Mentorship(models.Model):
    """A model that represents a mentorship (mentor<->project)"""
    mentor: Mentor = models.ForeignKey(Mentor, on_delete=models.PROTECT)
    project: Project = models.ForeignKey(Project, on_delete=models.PROTECT)
    from mentoring.utils import PROJECT_STATUS_CHOICES
    status = models.BooleanField(default=True, choices=PROJECT_STATUS_CHOICES)
