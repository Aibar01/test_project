from django.db import models


class Post(models.Model):
    preview = models.CharField(max_length=50)
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
