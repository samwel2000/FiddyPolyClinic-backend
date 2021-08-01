from typing import List
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import *
from .models import *



class NewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class JobsView(ListAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer


class TeamMembersView(ListAPIView):
    queryset = TeamMembers.objects.all()
    serializer_class = TeamMembersSerializer


class ContactUsView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
