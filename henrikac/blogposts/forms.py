from django import forms

from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Comment',
                'class': 'border border-info'
            })
        }
        labels = {
            'comment': ''
        }
