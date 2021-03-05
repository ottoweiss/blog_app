from django.db import models
from django.urls import reverse

#importing a class models (models.Model), then creating a subclass called Post
class Post(models.Model):
    #limiting characters to 200, and using ForeignKey, many-to-one, for storing the user's info. Also, it specifies to CASCADE
    #upon the foreingkey's deletion.
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    #creates text field for body that changes based on how many characters there are
    body = models.TextField()
    #returns a text string
    def __str__(self): 
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])




