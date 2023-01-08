from rest_framework import routers

from .views import CategoryViewSet, PhrasesViewSet


router = routers.DefaultRouter()  # add default basic root view
router.register('categories', CategoryViewSet)
router.register('phrases', PhrasesViewSet)

urlpatterns = router.urls
