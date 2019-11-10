from django.urls import path

from datatype.views import CreateView
from . import views

app_name = 'datatype'
urlpatterns = [
    path('create/<int:community_id>', CreateView.as_view(), name='create'),
    path('<int:community_id>', views.IndexView.as_view(), name='index'),
]
