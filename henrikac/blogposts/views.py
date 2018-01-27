from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from . import forms
from . import models


class BlogPostListView(generic.ListView):
    model = models.BlogPost
    paginate_by = 10


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


class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Comment
    login_url = 'users:login'

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'slug': self.object.post.slug})

    # just returning self.post because nothing is going to be rendered here
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    # if the user is not the author of the comment
    # or is a superuser
    # then the user will just be redirected away from the page
    def post(self, request, *args, **kwargs):
        user = self.request.user
        self.object = self.get_object()
        if not self.object.author == user.username or user.is_superuser:
            return HttpResponseRedirect(reverse('blog:list'))
        return self.delete(request, *args, **kwargs)
