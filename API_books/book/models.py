from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)
    author_of_book = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
