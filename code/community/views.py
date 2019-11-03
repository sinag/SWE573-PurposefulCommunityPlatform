from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
from .models import Community


class IndexView(generic.ListView):
    template_name = 'community/index.html'
    context_object_name = 'top_communities'

    def get_queryset(self):
        """
        Return top communities by post count
        """
        return Community.objects.order_by('-post_count')[:5]


class CreateView(CreateView):
    model = Community
    # fields = ['name']
    fields = "__all__"
    template_name = 'community/create.html'

    def get_success_url(self):
        return reverse('community:index')


class DeleteView(DeleteView):
    model = Community
    template_name = 'community/delete.html'
    success_url = reverse_lazy('community:index')

    def get_queryset(self):
        """
        Get community details to delete
        """
        return Community.objects.filter(id=self.kwargs.get('pk'))


class DetailView(generic.DetailView):
    model = Community
    template_name = 'community/detail.html'

    def get_queryset(self):
        """
        Get community details
        """
        return Community.objects.filter(id=self.kwargs.get('pk'))
