from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Author(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	books = models.ManyToManyField(Book, related_name="authors")
	notes = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


this_author = Author.objects.get(id=1)
book_a = Book.objects.get(id=1)
this_author.books.add(book_a)
