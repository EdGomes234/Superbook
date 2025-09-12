# EDGAR GOMES OLIVEIRA

from django.urls import path
from .views import PostCreateView, PostListView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('novo/', PostCreateView.as_view(), name='novo_post'),
    path('lista/', PostListView.as_view(), name='lista_posts'),
    path('<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('<int:pk>/excluir/', PostDeleteView.as_view(), name='excluir_post'),
]