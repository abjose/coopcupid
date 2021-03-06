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

    path('profiles/<int:pk>', views.ProfileDetailView.as_view(), name='profile_detail'),

    path('communities/', views.CommunityListView.as_view(), name='communities'),
    path('communities/<int:pk>', views.CommunityDetailView.as_view(), name='community_detail'),
    path('communities/<int:community_id>/posts/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('communities/<int:community_id>/events/<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
    path('communities/<int:community_id>/follow/', views.follow_community, name='follow_community'),
    path('community_search/', views.community_search, name='community_search'),

    path('opening/<int:pk>', views.OpeningDetailView.as_view(), name='opening_detail'),

    path('questions/', views.QuestionListView.as_view(), name='questions'),
    # path('questions/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail'),
    path('questions/<int:pk>', views.get_question_detail, name='question_detail'),

    # path('your-name/', views.get_name, name='your_name'),
]
