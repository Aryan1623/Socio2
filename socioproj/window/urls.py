from django.urls import path
from . import views

urlpatterns = [
    # Default index view
    path('', views.index, name='index'),

    # View for chat.html
    path('chat/', views.chat_view, name='chat'),

    # View for graphs.html
    path('graphs/', views.graph_view, name='graphs'),
]

