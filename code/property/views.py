from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView

from datatype.models import DataType
from property.models import Property


class IndexView(generic.ListView):
    template_name = 'property/index.html'
    context_object_name = 'properties'

    def get_queryset(self):
        # user = self.request.user.id
        """
        Return top communities by post count
        """
        return Property.objects.all().filter(datatype__id=self.kwargs.get('datatype_id')).order_by('created_on')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['subscriptions'] = Hotel.objects.all().order_by('star').reverse()[:3]
        # # Add any other variables to the context here
        return context


class CreateView(CreateView):
    model = Property
    fields = ['name', 'type']
    template_name = 'property/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.generic = False
        form.instance.datatype = DataType.objects.get(id=self.kwargs.get('datatype_id'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('property:index', kwargs={'datatype_id': self.kwargs.get('datatype_id')})
