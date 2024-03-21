from rest_framework import status
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.pagination import LimitOffsetPagination


# default size of limit is 20
class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20



class BookListAPIView(APIView):
    
    """this class is use to get details of books on search of book_id, topics, author name etc"""
    
    pagination_class = CustomLimitOffsetPagination
    def get(self, request, format=None):
        
        """this API is use to get details of books on search of book_id, topics, author name etc"""
        
        try:
            queryset = Book.objects.all()

            # Retrieve filter parameters from request query parameters
            book_id = request.query_params.get('book_id')
            language = request.query_params.get('language')
            mime_type = request.query_params.get('mime_type')
            topic = request.query_params.get('topic')
            author = request.query_params.get('author')
            title = request.query_params.get('title')
            
            
            if book_id:
                queryset = queryset.filter(gutenberg_id=book_id)
            if language:
                queryset = queryset.filter(languages__code=language)
            if mime_type:
                queryset = queryset.filter(format__mime_type=mime_type)
            if topic:
                topic_query = Q(subjects__name__icontains=topic) | Q(bookshelves__name__icontains=topic)
                queryset = queryset.filter(topic_query)
            if author:
                queryset = queryset.filter(authors__name__icontains=author)
            if title:
                queryset = queryset.filter(title__icontains=title)
                
            if not queryset.exists():
                return Response({'message': 'No books found.'}, status=status.HTTP_204_NO_CONTENT)

            
            #pagination
            paginator = self.pagination_class()
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = BookSerializer(paginated_queryset, many=True)   
            
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

