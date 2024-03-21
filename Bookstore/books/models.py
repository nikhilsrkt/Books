from django.db import models

class Author(models.Model):
    birth_year = models.SmallIntegerField(null=True)
    death_year = models.SmallIntegerField(null=True)
    name = models.CharField(max_length=128)
    class Meta:
        db_table = 'books_author'

class Book(models.Model):
    download_count = models.IntegerField(null=True)
    gutenberg_id = models.IntegerField(unique=True)
    media_type = models.CharField(max_length=16)
    title = models.TextField()
    authors = models.ManyToManyField(Author, through='BookAuthor')
    languages = models.ManyToManyField('Language', through='BookLanguage')
    subjects = models.ManyToManyField('Subject', through='BookSubject')
    bookshelves = models.ManyToManyField('Bookshelf', through='BookBookshelf')

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        db_table = 'books_book_authors'


class Bookshelf(models.Model):
    name = models.CharField(max_length=64)
    class Meta:
        db_table = 'books_bookshelf'

class BookBookshelf(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.CASCADE)
    class Meta:
        db_table = 'books_book_bookshelves'

class Language(models.Model):
    code = models.CharField(max_length=4)
    class Meta:
        db_table = 'books_language'

class BookLanguage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    class Meta:
        db_table = 'books_book_languages'

class Subject(models.Model):
    name = models.TextField()
    class Meta:
        db_table = 'books_subject'

class BookSubject(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class Meta:
        db_table = 'books_book_subjects'

class Format(models.Model):
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='formats')
    class Meta:
        db_table = 'books_format'
