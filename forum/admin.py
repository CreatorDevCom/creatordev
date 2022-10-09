from django.contrib import admin
from forum.models import Forum , Comment , GuestForum,GuestForumComment

# Register your models here.

admin.site.register(Forum)
admin.site.register(Comment)
admin.site.register(GuestForum)
admin.site.register(GuestForumComment)
