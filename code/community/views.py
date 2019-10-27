from django.views import generic
from .models import Community


class IndexView(generic.ListView):
    template_name = 'community/index.html'
    context_object_name = 'top_communities'

    def get_queryset(self):
        """
        Return top communities by post count
        """
        return Community.objects.order_by('-post_count')[:5]


class DetailView(generic.DetailView):
    model = Community
    template_name = 'community/detail.html'

    def get_queryset(self):
        """
        Get community details
        """
        return Community.objects.filter(id=self.kwargs.get('pk'))
