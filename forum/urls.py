from django.urls import path
from forum import views
urlpatterns = [
  path("",views.forumIndex , name="forum_index"),
  path("sendreply/<str:id>",views.sendReply , name="send_reply"),
  path("edit/<str:id>",views.eidtForum , name="edit_forum"),
  path("likecomment/<str:id>",views.likeComment , name="like_comment"),
  path("uploadforum",views.uploadForum , name="upload_forum"),
  path("likeforum/<str:id>",views.likeForum , name="like_forum"),
  path("createacomment/<str:id>",views.createAComment , name="create_a_comment"),
  path("preview/<str:id>",views.forumPreview , name="forum_preview"),
  path("guest/uploadforum",views.guestUpload , name="guest_upload"),
]
