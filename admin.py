from django.contrib import admin
from .models import User, ConsultationRequest

admin.site.register(User)
admin.site.register(ConsultationRequest)