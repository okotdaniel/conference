from django.contrib import admin
from app.models import Participants,Inquiries,CommiteeMembers,Contacts,Program,Papers


# Register your models here.
admin.site.register(Participants)
admin.site.register(Inquiries)
admin.site.register(CommiteeMembers)
admin.site.register(Contacts)
admin.site.register(Program)
admin.site.register(Papers)
