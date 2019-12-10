from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin

from datatype.models import DataType
from instance.models import Instance
from property.models import Property
from subscription.models import Subscription
from .models import Community


class IndexView(generic.ListView):
    template_name = 'community/index.html'
    context_object_name = 'communities'

    def get_queryset(self):
        return Community.objects.order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class CreateView(CreateView):
    model = Community
    fields = ['name', 'description']
    template_name = 'community/create.html'

    def form_valid(self, form):
        with transaction.atomic():
            form.instance.author = self.request.user
            form.instance.save()
            datatype = DataType(community=form.instance, author=self.request.user, name='Generic',
                                description='Generic post type for community ' + form.instance.name, generic=1)
            datatype.save()
            property_title = Property(datatype=datatype, author=self.request.user, name='Title', type=0, generic=1,
                                      required=True)
            property_title.save()
            property_description = Property(datatype=datatype, author=self.request.user, name='Description',
                                            type=0, generic=1,
                                            required=True)
            property_description.save()
            property_semantic_tag = Property(datatype=datatype, author=self.request.user, name='Semantic Tags',
                                             type=0, generic=1, required=True)
            property_semantic_tag.save()
            return FormMixin.form_valid(self, form)
            # return super().form_valid(form)

    def get_success_url(self):
        return reverse('community:index')


@receiver(post_save, sender=Community)
def create_initial_member(sender, instance, **kwargs):
    a = Subscription(user=instance.author, community=instance)
    a.save()


class UpdateView(UpdateView):
    model = Community
    fields = ['name', 'description']
    template_name = 'community/update.html'

    def get_success_url(self):
        return reverse('community:index')

    def get_queryset(self):
        """
        Get community details to update
        """
        return Community.objects.filter(id=self.kwargs.get('pk'))


class DeleteView(DeleteView):
    model = Community
    template_name = 'community/delete.html'

    def get_success_url(self):
        return reverse('community:index')

    def get_queryset(self):
        """
        Get community details to delete
        """
        return Community.objects.filter(id=self.kwargs.get('pk'))


class PostsView(generic.ListView):
    model = Instance
    template_name = 'community/posts.html'
    context_object_name = 'instances'

    def get_queryset(self):
        """
        Get community details
        """
        return Instance.objects.filter(
            datatype_id__in=DataType.objects.all().filter(community_id=self.kwargs.get('pk'))).order_by('-created_on')
