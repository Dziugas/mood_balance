from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.slugField()
    body = models.textField()
    date = models.DateTimeField(auto_now_add=True)

#add in later:
#    thumbnail
#    author
