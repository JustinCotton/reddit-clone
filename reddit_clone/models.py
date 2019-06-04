from django.db import models          

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password= models.CharField(max_length=100)

    def __str__(self):
        return self.username


# class Song(models.Model):
#     title = models.CharField(max_length=100)
#     album = models.CharField(max_length=100)
#     preview_url = models.TextField(null=True, blank=True)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    
#     def __str__(self):
#         return self.title 

# class Favorite(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='favorites')
#     song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='favorites')
    