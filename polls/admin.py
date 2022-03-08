from django.contrib import admin

from .models import Community, Membership, Question

admin.site.register(Community)
admin.site.register(Membership)
admin.site.register(Question)
