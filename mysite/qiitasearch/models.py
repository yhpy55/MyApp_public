from django.db import models

class QiitaSearch(models.Model):
    qid = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=100,null=True)
    created_at = models.CharField(max_length=30)
    updated_at = models.CharField(max_length=30)
    comments_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    reactions_count = models.IntegerField(default=0)

    def __str__(self):
        return f'<QiitaSearch:id= {self.title} {self.url}>'