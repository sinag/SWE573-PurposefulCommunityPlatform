from django.urls import path
from instance.views import CreateView

app_name = 'instance'
urlpatterns = [
    path('create/<int:datatype_id>', CreateView.as_view(), name='create'),
]
