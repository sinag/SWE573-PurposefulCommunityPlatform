from django import forms


class CreatePost(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CreatePost, self).__init__(*args, **kwargs)


class DeletePost(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DeletePost, self).__init__(*args, **kwargs)
