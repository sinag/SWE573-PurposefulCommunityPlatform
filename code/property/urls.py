from django.urls import path
from . import views

app_name = 'property'
urlpatterns = [
    path('<int:datatype_id>', views.IndexView.as_view(), name='index'),
]
