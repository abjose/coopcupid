from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Community


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class UserListView(generic.ListView):
    model = User
    paginate_by = 30
    ordering = ["name"]
    template_name = 'polls/user_list.html'


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'polls/user_detail.html'


class CommunityListView(generic.ListView):
    model = Community
    paginate_by = 30
    ordering = ["name"]
    template_name = 'polls/community_list.html'


class CommunityDetailView(generic.DetailView):
    model = Community
    template_name = 'polls/community_detail.html'
