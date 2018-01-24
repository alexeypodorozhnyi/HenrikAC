from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from . import forms
from . import models


class BlogPostListView(generic.ListView):
    model = models.BlogPost


# https://docs.djangoproject.com/en/1.8/topics/class-based-views/mixins/#using-formmixin-with-detailview
class BlogPostDetailView(FormMixin, generic.DetailView):
    model = models.BlogPost
    form_class = forms.CommentForm

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = models.Comment.objects.filter(post=self.object)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        author = self.request.user.username

        if self.request.user.is_superuser:
            author = 'Admin'

        models.Comment.objects.create(
            post=self.object,
            comment=form.cleaned_data['comment'],
            author=author,
        )
        return super().form_valid(form)
