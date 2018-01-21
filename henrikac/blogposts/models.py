from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    category = models.CharField(max_length=40)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
