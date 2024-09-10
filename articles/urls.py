# from django.urls import path
# from .views import list_article, formulaireArtist, deleteArticle,updateArticle

# app_name = 'article'

# urlpatterns = [
    
#     path('liste/',list_article, name='list_article' ),
#     path('formulaire/', formulaireArtist, name='formulaireArtist'), 
#     path('delete/<int:id>/', deleteArticle, name='delete_article'),
#     path('edit/<int:id>/', updateArticle, name='update_article'),
# ]

from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView,AddCommentView

app_name = 'article'

urlpatterns = [
    path('', ArticleListView.as_view(), name='list_article'),
    path('new/', ArticleCreateView.as_view(), name='new_article'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='update_article'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete_article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    ]

