from rest_framework import routers
from django.urls import path

from rest_framework_nested.routers import NestedSimpleRouter

from .views import CategoryViewSet, PhrasesViewSet
from . import views

router = routers.DefaultRouter()  # add default basic root view
router.register('categories', CategoryViewSet)
router.register('phrases', PhrasesViewSet)

categories_router = NestedSimpleRouter(router, r'categories', lookup='category')
categories_router.register(r'phrases', PhrasesViewSet)

urlpatterns = router.urls

# urlpatterns = router.urls + categories_router.urls + [
#     path('api/categories/<int:pk>/phrases/<int:phrase_id>/filter_by_id/', views.CategoryViewSet.as_view({'get': 'filter_by_id'}), name='filter_by_id')
#     ]