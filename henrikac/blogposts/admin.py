from django.contrib import admin

from . import models


class BlogPostAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'content',
        'category',
        'is_live',
    )


admin.site.register(models.BlogPost, BlogPostAdmin)
