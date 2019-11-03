from django.urls import path

from community.views import CreateView, DeleteView
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/delete', DeleteView.as_view(), name='delete'),
    path('create', CreateView.as_view(), name='create'),
]