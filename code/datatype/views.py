from django.db import transaction
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin, FormView

from datetimefield.models import DateTimeField
from instance.models import Instance
from integerfield.models import IntegerField
from property.models import Property
from textfield.models import TextField
from .forms import SearchForm
from .models import DataType
from community.models import Community


class IndexView(generic.ListView):
    template_name = 'datatype/index.html'
    context_object_name = 'datatypes'

    def get_queryset(self):
        # user = self.request.user.id
        """
        Return top communities by post count
        """
        return DataType.objects.all().filter(community__id=self.kwargs.get('community_id')).order_by(
            'generic').order_by('created_on')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # context['subscriptions'] = Hotel.objects.all().order_by('star').reverse()[:3]
        # # Add any other variables to the context here
        return context


class CreateView(CreateView):
    model = DataType
    fields = ['name', 'description']
    template_name = 'datatype/create.html'

    def form_valid(self, form):
        with transaction.atomic():
            form.instance.author = self.request.user
            form.instance.generic = False
            form.instance.community = Community.objects.get(id=self.kwargs.get('community_id'))
            form.instance.save()
            property_title = Property(datatype=form.instance, author=self.request.user, name='Title', type=0, generic=1,
                                      required=True)
            property_title.save()
            property_semantic_tag = Property(datatype=form.instance, author=self.request.user, name='Semantic Tags',
                                             type=0, generic=1, required=True)
            property_semantic_tag.save()
            return FormMixin.form_valid(self, form)
            # return super().form_valid(form)

    def get_success_url(self):
        return reverse('datatype:index', kwargs={'community_id': self.kwargs.get('community_id')})


class DeleteView(DeleteView):
    model = DataType
    template_name = 'datatype/delete.html'

    def get_success_url(self):
        return reverse('datatype:index', kwargs={'community_id': self.kwargs.get('community_id')})

    def get_queryset(self):
        """
        Get datatype details to delete
        """
        return DataType.objects.filter(id=self.kwargs.get('pk'))


class UpdateView(UpdateView):
    model = DataType
    fields = ['name', 'description']
    template_name = 'datatype/update.html'

    def get_success_url(self):
        return reverse('datatype:index', kwargs={'community_id': self.kwargs.get('community_id')})

    def get_queryset(self):
        """
        Get community details to delete
        """
        return DataType.objects.filter(id=self.kwargs.get('pk'))


class SearchView(FormView):
    template_name = 'datatype/search.html'
    form_class = SearchForm

    def form_valid(self, form):
        self.request.session['search_data'] = form.data
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('datatype:result', kwargs={'community_id': self.kwargs.get('community_id'),
                                                  'datatype_id': self.kwargs.get('datatype_id')})


class ResultView(generic.ListView):
    model = Instance
    template_name = 'datatype/results.html'
    context_object_name = 'instances'

    def get_queryset(self):
        """
        Get search results
        """
        search_data = self.request.session.get('search_data')
        for instance in Instance.objects.all():
            instance_id = instance.id
            for field in DataType.objects.get(id=self.kwargs.get('datatype_id')).fields():
                search_keyword = search_data[field.name]
                if field.type == 0 or field.type == 4 or field.type == 5 or field.type == 6 or field.type == 7 or field.type == 8:
                    field_value = TextField.objects.filter(instance_id=instance.id).filter(
                        property_id=field.id).first()
                if field.type == 1:
                    field_value = IntegerField.objects.filter(instance_id=instance.id).filter(
                        property_id=field.id).first()
                if field.type == 2:
                    field_value = DateTimeField.objects.filter(instance_id=instance.id).filter(
                        property_id=field.id).first()

        return Instance.objects.filter(
            datatype_id__in=DataType.objects.all().filter(community_id=self.kwargs.get('community_id'))).order_by(
            '-created_on')
