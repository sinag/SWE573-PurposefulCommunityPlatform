from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView
from .models import DataType


class IndexView(generic.ListView):
    template_name = 'datatype/index.html'
    context_object_name = 'datatypes'

    def get_queryset(self):
        # user = self.request.user.id
        """
        Return top communities by post count
        """
        return DataType.objects.all().filter(community__id=self.kwargs.get('community_id')).order_by('created_on')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['subscriptions'] = Hotel.objects.all().order_by('star').reverse()[:3]
        # # Add any other variables to the context here
        return context

# class CreateView(CreateView):
#     model = DataType
#     fields = ['name', 'description', 'post_count']
#     template_name = 'datatype/create.html'
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('datatype:index')  # Todo - this will go to datatypes form
