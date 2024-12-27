from django.db import models

class blogs(models.Model):
    blog_name = models.TextField(max_length=50)
    blog_content = models.TextField(max_length=1000)
