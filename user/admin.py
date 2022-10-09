from django.contrib import admin

from user.models import UserProfile , Action , Inbox , CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserProfile)
admin.site.register(Action)
admin.site.register(Inbox)