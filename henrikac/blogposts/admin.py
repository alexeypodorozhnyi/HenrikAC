from django.contrib import admin

from . import models


class CommentInline(admin.StackedInline):
    model = models.Comment


class BlogPostAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'content',
        'category',
        'is_live',
    )
    inlines = [
        CommentInline,
    ]


admin.site.register(models.BlogPost, BlogPostAdmin)
