from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='Email address')
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label='Leave empty')

    def clean(self):
        cleaned_data = super().clean()
        honeypot = cleaned_data['honeypot']
        if len(honeypot) > 0:
            raise forms.ValidationError(
                'Honeypot should be left empty. Bad bot!'
            )
