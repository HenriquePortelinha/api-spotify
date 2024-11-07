from rest_framework import viewsets, generics
from .serializers import LivrosSerializer
from ..models import Users, Livros


class LivrosViewSet(viewsets.ModelViewSet):
    model = Livros
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
    lookup_field = 'id_books'
    
    