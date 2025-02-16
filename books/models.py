from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=20)
    genre = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    cover = models.CharField(max_length=300)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
