from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic

from . import forms


class ContactView(generic.FormView):
    form_class = forms.ContactForm
    template_name = 'contacts/contact.html'
    success_url = reverse_lazy('contact:contact_me')

    def form_valid(self, form):
        send_mail(
            'Contact from henrikac.com',
            'From {name} <{email}>\n\n{message}'.format(**form.cleaned_data),
            'henrik.abel@henrikac.com',
            ['henrik.abel@henrikac.com']
        )
        messages.success(
            self.request,
            'Thank you very much for your message. I will get back to you as soon as possible'
        )
        return super().form_valid(form)
