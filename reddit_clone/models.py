from django.db import models          

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password= models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    created_at = models.DateField()
    title = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    site_url = models.TextField()
    vote_total = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')

    def __str__(self):
        return self.title

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
    vote_total = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.created_at
