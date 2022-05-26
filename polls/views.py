from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .filters import CommunityFilter
from .forms import ChoiceResponseForm
from .models import Community, Question, ChoiceResponse, Membership, Post, Event, Profile


class IndexView(generic.ListView):
    template_name = 'polls/index.html'

    def get_queryset(self):
        # return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return []


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # if self.request.user.id
        print(f"user id: {self.request.user.id}")

        if self.request.user.id:
            context['posts'] = []
            context['events'] = []

            profile = Profile.objects.get(user=self.request.user)

            for membership in Membership.objects.filter(profile=profile):
                context['posts'] += Post.objects.filter(community=membership.community)
                context['events'] += Event.objects.filter(community=membership.community)

            print(f"found {len(context['posts'])} posts and {len(context['events'])} events")
        else:
            print("not logged in")

        return context


class UserListView(generic.ListView):
    model = User
    paginate_by = 30
    ordering = ["name"]
    template_name = 'polls/user_list.html'


class CommunityListView(generic.ListView):
    model = Community
    paginate_by = 30
    ordering = ["name"]
    template_name = 'polls/community_list.html'


class QuestionListView(generic.ListView):
    model = Question
    paginate_by = 30
    ordering = ["pub_date"]
    template_name = 'polls/question_list.html'


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'polls/user_detail.html'


class CommunityDetailView(generic.DetailView):
    model = Community
    template_name = 'polls/community_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityDetailView, self).get_context_data(**kwargs)

        context['memberships'] = Membership.objects.filter(community=self.object.id)

        return context


class PostDetailView(generic.DetailView):
    model = Community
    template_name = 'polls/community_detail.html'


class EventDetailView(generic.DetailView):
    model = Community
    template_name = 'polls/community_detail.html'


def community_search(request):
    f = CommunityFilter(request.GET, queryset=Community.objects.all())
    return render(request, 'polls/community_search.html', {'filter': f})


def get_question_detail(request, pk=None):
    question = Question.objects.get(pk=pk)

    if not request.user.is_authenticated:
        form = ChoiceResponseForm()
        return render(request, 'polls/question_detail.html', {'object': question, 'form': form})

    choices = ChoiceResponse.objects.filter(question=question, user=request.user)
    if len(choices) == 0:
        choice = ChoiceResponse(question=question, user=request.user)
    else:
        assert(len(choices) == 1)
        choice = choices[0]

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ChoiceResponseForm(request.POST, instance=choice)  # will this overwrite new values?
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            return HttpResponseRedirect('/polls/questions/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ChoiceResponseForm(instance=choice)

    return render(request, 'polls/question_detail.html', {'object': question, 'form': form})
