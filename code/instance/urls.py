from django.urls import path
from instance.views import CreateView, DeleteView

app_name = 'instance'
urlpatterns = [
    path('create/<int:datatype_id>', CreateView.as_view(), name='create'),
    path('delete/<int:datatype_id>/<int:pk>', DeleteView.as_view(), name='delete'),
]
