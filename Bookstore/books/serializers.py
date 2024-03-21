from rest_framework import serializers
from .models import Book, Format
from rest_framework import serializers
from .models import Book, Author, Language, Subject, Bookshelf

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_year', 'death_year']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['code']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name']
        
class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ['name']
        
class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = ['mime_type', 'url']
        


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    bookshelves = BookshelfSerializer(many=True, read_only=True)
    formats = FormatSerializer(many=True, read_only=True)
    

    class Meta:
        model = Book
        fields = ['gutenberg_id', 'title', 'authors', 'title','languages', 'subjects', 'bookshelves','download_count','media_type','formats']
        
    def get_mime_type(self, obj):
        return obj.formats.first().mime_type if obj.formats.exists() else None

    def get_url(self, obj):
        return obj.formats.first().url if obj.formats.exists() else None
