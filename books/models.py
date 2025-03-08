from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


from django.contrib.auth.models import User

class Books(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    authors = models.ManyToManyField("Author")

    def __str__(self):
        return self.title

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.book.title}"