from rest_framework.routers import SimpleRouter
from .viewsets import JokesViewSet

router = SimpleRouter()

router.register('random-jokes', JokesViewSet, basename='random')