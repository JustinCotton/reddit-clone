from django.db import models

class Post(models.Model):
    created_at = models.TextField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    site_url = models.TextField(null=True, blank=True)
    vote_total = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return self.title

class Comment(models.Model):
    created_at = models.DateField()
    content = models.TextField()
    vote_total = models.IntigerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.created_at
