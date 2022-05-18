from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import JokesSerializer
from chucknorris.models import Jokes


class JokesViewSet(ModelViewSet):
    serializer_class = JokesSerializer
    queryset = Jokes.objects.none()
    model = Jokes

    def list(self, *args, **kwargs):
        results = Jokes.random_jokes()
        serializer = JokesSerializer(results, many=True)
        return Response({ 'jokes': serializer.data, 'length': len(results)})

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
