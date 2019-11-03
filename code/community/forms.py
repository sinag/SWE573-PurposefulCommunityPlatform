from django import forms
from community.models import Community


class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = "__all__"
