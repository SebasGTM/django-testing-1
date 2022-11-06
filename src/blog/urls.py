from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
)

app_name = "articles"
urlpatterns = [
     path('', ArticleListView.as_view(), name="article-list"),
     path('create/', ArticleCreateView.as_view(), name="article_create"),
     path('<int:id>/', ArticleDetailView.as_view(), name="article-details"),
]

