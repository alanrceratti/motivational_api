from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .models import Category, Phrases
from .serializers import CategorySerializer, PhrasesSerializer


# CRUD Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
     # retrieve all phrases from a category and filter by id from category and phrase- example:
#http://127.0.0.1:200/api/categories/1/phrases/
#http://127.0.0.1:200/api/categories/1/phrases/?filter_by_id=1
    @action(detail=True, methods=['get'])
    def phrases(self, request, pk=None):
        category = self.get_object()
        phrase_id = request.query_params.get('filter_by_id', None)
        if phrase_id is not None:
            phrases = get_object_or_404(category.phrases, pk=phrase_id)
            serializer = PhrasesSerializer(phrases)
            return Response(serializer.data)
        else:
            phrases = category.phrases.all()
        serializer = PhrasesSerializer(phrases, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def all(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

# CRUD Phrases
class PhrasesViewSet(viewsets.ModelViewSet):
    queryset = Phrases.objects.all()
    serializer_class = PhrasesSerializer


    



   

