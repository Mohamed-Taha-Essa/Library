from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    biography = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10 ,decimal_places=2)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    content = models.TextField()
    rate =[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]

    rating = models.IntegerField(choices=rate)

    def __str__(self):
        return f"{self.book.title}"
    