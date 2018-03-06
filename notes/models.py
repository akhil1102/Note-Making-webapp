from django.db import models
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200,null=True)
    body = models.TextField()

    def get_absolute_url(self):
        return "/notes/detail/%s/" % (self.id)





