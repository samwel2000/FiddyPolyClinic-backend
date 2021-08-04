from django.urls import path
from .views import *

urlpatterns = [
    path('news-list/', NewsView.as_view(), name="news-list"),
    path('jobs-list/', JobsView.as_view(), name="jobs-list"),
    path('team-members-list/', TeamMembersView.as_view(), name="team-members-list"),
    path('message-create/', ContactUsView.as_view(), name="message-create"),
    path('subscribe/', SubscribersView.as_view(), name="subscribe"),
]
