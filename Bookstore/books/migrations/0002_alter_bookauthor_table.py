# Generated by Django 5.0.3 on 2024-03-21 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookauthor',
            table='books_book_authors',
        ),
    ]