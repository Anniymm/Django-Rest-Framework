from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    published_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title