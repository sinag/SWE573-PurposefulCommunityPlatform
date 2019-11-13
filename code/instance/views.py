from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, FormView

from datatype.models import DataType
from instance.forms import MyForm
from .models import Instance


class CreateView(CreateView):
    model = Instance
    template_name = 'instance/create.html'
    form_class = MyForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.datatype = DataType.objects.get(id=self.kwargs.get('datatype_id'))
        a = form.cleaned_data.get('name')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('community:posts',
                       kwargs={'pk': DataType.objects.get(id=self.kwargs.get('datatype_id')).community.id})
