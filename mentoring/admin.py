from django.contrib import admin
from mentoring.models import Mentor, Project, Mentorship


admin.site.register([Mentor, Project, Mentorship])
