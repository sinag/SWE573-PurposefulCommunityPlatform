from django import forms

from instance.models import Instance


class MyForm(forms.ModelForm):
    class Meta:
        model = Instance
        fields = []
    name = forms.CharField(label='name', max_length=100)
