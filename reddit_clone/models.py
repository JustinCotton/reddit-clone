from django.db import models

class Comment(models.Model):
    created_at = models.DateField()
    content = models.TextField()
    vote_total = models.IntigerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.created_at