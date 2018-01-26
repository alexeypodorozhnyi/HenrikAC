from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Email address'

    def clean_username(self):
        username = self.cleaned_data['username']
        excluded_usernames = ['admin', 'adm1n', '@dmin', '@dm1n']

        if username.lower() in excluded_usernames:
            raise forms.ValidationError('That is not a valid username')
        return username
