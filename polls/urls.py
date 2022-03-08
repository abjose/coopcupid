from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # path('topics/', views.TopicListView.as_view(), name='topics'),
    # path('topics/search/', views.TopicSearchResultsView.as_view(), name='topic_search_results'),
    # path('topics/<int:pk>/', views.TopicDetailView.as_view(), name='topic_detail'),
    # path('resources/<int:pk>/', views.ResourceDetailView.as_view(), name='resource_detail'),
    # path('goals/<int:pk>/', views.GoalDetailView.as_view(), name='goal_detail'),

    path('users/', views.UserListView.as_view(), name='users'),
    path('users/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    
    path('communities/', views.CommunityListView.as_view(), name='communities'),
    path('communities/<int:pk>', views.CommunityDetailView.as_view(), name='community_detail'),
    path('community_search/', views.community_search, name='community_search'),

    path('questions/', views.QuestionListView.as_view(), name='qiestopms'),
    path('questions/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail'),
]
