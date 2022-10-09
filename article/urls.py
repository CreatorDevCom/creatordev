from django.urls import path
from article import views
# 
urlpatterns = [
  path('',views.articleIndex , name='article_home'),
  path('createnew',views.createNew , name='create_new'),
  path('edit/<str:id>',views.editArticle , name='edit_article'),
  path('likearticle/<str:article_id>',views.likeArticle , name='like_article'),
  path('likecomment/<str:commentId>',views.likeComment , name='like_comment'),
  path('postacomment/<str:id>',views.postAComment , name='post_a_comment'),
  path('sendreply/<int:id>',views.sendReplay , name='sent_replay'), 
  # path('getarticlesof/<str:username>',views.getArticleForASpecificUser , name='get_article_for_username'),
  path('<str:id>',views.previewArticle , name='article_preview'),
]
