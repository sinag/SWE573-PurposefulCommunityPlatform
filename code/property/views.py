from django.views import generic
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
