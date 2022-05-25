from django.contrib import admin

from .models import Community, Membership, Question, ChoiceResponse, Post, Event, Profile

admin.site.register(Community)
admin.site.register(Membership)
admin.site.register(Question)
admin.site.register(ChoiceResponse)
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Profile)
