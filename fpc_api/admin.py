from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.site_header = "Fiddy Polyclinic administration"
admin.site.site_title = "Fiddy Polyclinic admin site"
admin.site.unregister(Group)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['heading', 'created_date', ]
    model = News


admin.site.register(News, NewsAdmin)


class JobsAdmin(admin.ModelAdmin):
    list_display = ['title', 'position_number', 'created_date']
    list_filter = ('title',)
    model = Jobs


admin.site.register(Jobs, JobsAdmin)


class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'position']
    list_filter = ('position',)
    model = TeamMembers


admin.site.register(TeamMembers, TeamMembersAdmin)


class ContactUssAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number']
    model = ContactUs


admin.site.register(ContactUs, ContactUssAdmin)
