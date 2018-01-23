from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=80, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=40)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_live = models.BooleanField(default=False)
    slug = models.SlugField(max_length=80)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField()
    author = models.CharField(max_length=40)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return 'Comment from <{}> to <{}>'.format(self.author, self.post.title)
