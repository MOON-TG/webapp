from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()

  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  #autor : 추후 예정

  def __str__(self):
    return f'{self.title}'

  def get_absolute_url(self):
    return f'/blog/{self.pk}'

