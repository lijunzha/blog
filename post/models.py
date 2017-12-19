from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def get_comment(self):
        return Comment.objects.filter(aid=self.id)


class Comment(models.Model):
    aid = models.IntegerField()
    name = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
