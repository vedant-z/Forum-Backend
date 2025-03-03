from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Answer(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) #updated_date can also be used to check if edited
    content = models.TextField()
    # question_related = models.ForeignKey(Question, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='NO USER')

    def __str__(self):  
        return str(self.id)