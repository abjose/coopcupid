from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .filters import CommunityFilter
from .forms import ChoiceResponseForm
from .models import Community, Question, ChoiceResponse


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


class UserDetailView(generic.DetailView):
    model = User
    template_name = 'polls/user_detail.html'


class CommunityDetailView(generic.DetailView):
    model = Community
    template_name = 'polls/community_detail.html'


def community_search(request):
    f = CommunityFilter(request.GET, queryset=Community.objects.all())
    return render(request, 'polls/community_search.html', {'filter': f})


def get_question_detail(request, pk=None):
    question = Question.objects.get(pk=pk)

    if not request.user:
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
