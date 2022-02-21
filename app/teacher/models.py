from django.db import models

# → Here is defined the database where the teachers will store the papers they upload.
class papers(models.Model):
    title = models.CharField(max_length=1024)
    p_id = models.CharField(max_length=1024)
    authors = models.CharField(max_length=1024)
    file = models.CharField(max_length=1024)
    category = models.CharField(max_length=1024)
    keywords = models.CharField(max_length=1024)



