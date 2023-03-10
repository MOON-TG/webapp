from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=30)
  content = models.TextField()

  head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
  head_image2 = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)

  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)
  #autor : μΆν μμ 

  def __str__(self):
    return f'{self.title}'

  def get_absolute_url(self):
    return f'/blog/{self.pk}'



