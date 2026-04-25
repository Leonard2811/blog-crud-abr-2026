from django.urls import path
from .views import (ArticleListView, 
                    ArticleDetailView, 
                    ArticleCreateView,)

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'), 
    path('articulos/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articulos/nuevo/', ArticleCreateView.as_view(), name='article_create'),
]