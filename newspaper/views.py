from django.views.generic import ListView,DetailView, CreateView
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'articles-list.html'
    context_object_name = 'articles_list'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article-detail.html'
    context_object_name = 'article'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article-create.html'
    fields = ['title', 'content', 'author']
