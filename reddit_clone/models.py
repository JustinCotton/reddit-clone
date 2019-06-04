from django.db import models          

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password= models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Comment(models.Model):
    created_at = models.DateField()
    content = models.TextField()
    vote_total = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.created_at
