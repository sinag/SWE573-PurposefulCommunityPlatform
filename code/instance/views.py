from django.db import transaction
from django.urls import reverse
from django.views.generic import FormView
from datatype.models import DataType
from instance.forms import CreatePost, DeletePost
from integerfield.models import IntegerField
from textfield.models import TextField
from .models import Instance


class CreateView(FormView):
    template_name = 'instance/create.html'
    form_class = CreatePost

    def form_valid(self, form):
        with transaction.atomic():
            instance = Instance(datatype=DataType.objects.get(id=self.kwargs.get('datatype_id')),
                                author=self.request.user)
            instance.save()
            for field in DataType.objects.get(id=self.kwargs.get('datatype_id')).fields():
                if field.type == 0:  # Todo - handle all datatypes
                    value = TextField(value=form.data[field.name], property_id=field.id, instance_id=instance.id)
                    value.save()
                if field.type == 1:
                    if form.data[field.name] is not '':
                        value = IntegerField(value=int(form.data[field.name]), property_id=field.id,
                                             instance_id=instance.id)
                    else:
                        value = IntegerField(value=None, property_id=field.id,
                                             instance_id=instance.id)
                    value.save()

            return super().form_valid(form)

    def get_success_url(self):
        return reverse('community:posts',
                       kwargs={'pk': DataType.objects.get(id=self.kwargs.get('datatype_id')).community.id})


class DeleteView(FormView):
    template_name = 'instance/delete.html'
    form_class = DeletePost

    def form_valid(self, form):
        with transaction.atomic():
            instance = Instance.objects.get(id=self.kwargs.get('pk'))
            for field in DataType.objects.get(id=instance.datatype_id).fields():
                if field.type == 0:  # Todo - handle all datatypes
                    value = TextField.objects.filter(instance_id=instance.id).filter(property_id=field.id)
                    value.delete()
                if field.type == 1:
                    value = IntegerField.objects.filter(instance_id=instance.id).filter(property_id=field.id)
                    value.delete()
            instance.delete()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('community:posts',
                       kwargs={'pk': DataType.objects.get(id=self.kwargs.get('datatype_id')).community.id})
