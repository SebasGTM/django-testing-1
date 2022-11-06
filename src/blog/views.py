from django.shortcuts import get_object_or_404, render

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

# Create your views here.

from .models import Article
from .forms import ArticleForm


class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    form_class = ArticleForm
    queryset = Article.objects.all()

class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = "articles/article_details.html"
    queryset = Article.objects.all()

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Article, id = _id)