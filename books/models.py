from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    cover = models.ImageField(upload_to='illustrations/')
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
