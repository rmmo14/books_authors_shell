
## Query: Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
>>> from books_authors_app.models import *
>>> Book.objects.create(title="C Sharp")
<Book: Book object (1)>
>>> Book.objects.create(title="Java")
<Book: Book object (2)>
>>> Book.objects.create(title="Python")
<Book: Book object (3)>
>>> Book.objects.create(title="PHP")
<Book: Book object (4)>
>>> Book.objects.create(title="Ruby")
<Book: Book object (5)>

## Query:Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu
>>> Author.objects.create(first_name="Jane", last_name="Austen")
<Author: Author object (1)>
>>> Author.objects.create(first_name="Emily", last_name="Dickinson")
<Author: Author object (2)>
>>> Author.objects.create(first_name="Fyodor", last_name="Dostoevsky")
<Author: Author object (3)>
>>> Author.objects.create(first_name="William", last_name="Shakespeare")
<Author: Author object (4)>
>>> Author.objects.create(first_name="Lau", last_name="Tzu")
<Author: Author object (5)>

## Query: Change the name of the C Sharp book to C#
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>, <Book: Book object (4)>, <Book: Book object (5)>]>
>>> c = Book.objects.get(id=1)
>>> c.title = "C#"
>>> c.save()

## Query: Change the first name of the 4th author to Bill
>>> a = Author.objects.get(id=4)
>>> a.first_name="Bill"
>>> a.save()

## Query: Assign the first author to the first 2 books
>>> this_author = Author.objects.get(id=1)
>>> book_a = Book.objects.get(id=1)
>>> this_author.books.add(book_a)
>>> book_b = Book.objects.get(id=2)
>>> this_author.books.add(book_b)
>>> this_author.books.all()

## Query: Assign the second author to the first 3 books
>>> second_author = Author.objects.get(id=2)
>>> second_author.books.add(book_a)
>>> second_author.books.add(book_b)
>>> book_c = Book.objects.get(id=3)
>>> second_author.books.add(book_c)

## Query: Assign the third author to the first 4 books
>>> book_d = Book.objects.get(id=4)
>>> third_author = Author.objects.get(id=3)
>>> third_author.books.add(book_a)
>>> third_author.books.add(book_b)
>>> third_author.books.add(book_c)
>>> third_author.books.add(book_d)

## Query: Assign the fourth author to the first 5 books (or in other words, all the books)
>>> book_e = Book.objects.get(id=5)
>>> fourth_author = Author.objects.get(id=4)
>>> fourth_author.books.add(book_a)
>>> fourth_author.books.add(book_b)
>>> fourth_author.books.add(book_c)
>>> fourth_author.books.add(book_d)
>>> fourth_author.books.add(book_e)

## Query: Retrieve all the authors for the 3rd book
>>> book_c.authors.all()
<QuerySet [<Author: Author object (2)>, <Author: Author object (3)>, <Author: Author object (4)>]>

## Query: Remove the first author of the 3rd book
>>> book_c.authors.remove(second_author)
>>> book_c.authors.all()
<QuerySet [<Author: Author object (3)>, <Author: Author object (4)>]>

## Query: Add the 5th author as one of the authors of the 2nd book
>>> fifth_author = Author.objects.get(id=5)
>>> book_b.authors.add(fifth_author)

## Query: Find all the books that the third author is a part of
>>> third_author.books.all()
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>, <Book: Book object (4)>]>

## Query: Find all the authors that contributed to the 5th book
>>> book_a.authors.all()
<QuerySet [<Author: Author object (1)>, <Author: Author object (2)>, <Author: Author object (3)>, <Author: Author object (4)>]>