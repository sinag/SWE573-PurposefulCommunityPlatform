from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Community


class IndexView(generic.ListView):
    template_name = 'community/index.html'
    context_object_name = 'top_communities'

    def get_queryset(self):
        # user = self.request.user.id
        """
        Return top communities by post count
        """
        return Community.objects.order_by('-post_count')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['subscriptions'] = Hotel.objects.all().order_by('star').reverse()[:3]
        # # Add any other variables to the context here
        return context


class CreateView(CreateView):
    model = Community
    fields = ['name', 'description', 'post_count']
    template_name = 'community/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('community:index')


class UpdateView(UpdateView):
    model = Community
    fields = ['name', 'description', 'post_count']
    template_name = 'community/update.html'

    def get_success_url(self):
        return reverse('community:index')

    def get_queryset(self):
        """
        Get community details to delete
        """
        return Community.objects.filter(id=self.kwargs.get('pk'))


class DeleteView(DeleteView):
    model = Community
    template_name = 'community/delete.html'
    success_url = reverse_lazy('community:index')

    def get_success_url(self):
        return reverse('community:index')

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
