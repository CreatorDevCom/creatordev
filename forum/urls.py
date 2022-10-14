from django.urls import path
from forum import views
urlpatterns = [
  path("",views.forumIndex , name="forum_index"),
  path("sendreply/<int:id>",views.sendReply , name="send_reply"),
  path("edit/<int:id>",views.eidtForum , name="edit_forum"),
  path("likecomment/<str:id>",views.likeComment , name="like_comment"),
  path("uploadforum",views.uploadForum , name="upload_forum"),
  path("likeforum/<int:id>",views.likeForum , name="like_forum"),
  path("createacomment/<int:id>",views.createAComment , name="create_a_comment"),
  path("preview/<int:id>",views.forumPreview , name="forum_preview"), 
]
