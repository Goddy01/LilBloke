from django.db import models
from accounts.models import UserAccount
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    movie_id = models.IntegerField(blank=False, null=False)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)