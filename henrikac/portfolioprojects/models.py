from django.db import models


class PortfolioProject(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    photo_file_name = models.CharField(max_length=80)
    url = models.CharField(max_length=80)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return 'Project: {}'.format(self.title)
