from django.db.models import fields
from rest_framework import serializers
from .models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'


class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        exclude = ['created_date']


class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        exclude = ['created_date']
