from rest_framework.routers import DefaultRouter
from django.urls import path ,include
from .views import CreateBookViewSet

router= DefaultRouter()
router.register(r'createbook',CreateBookViewSet,basename='createbook')
urlpatterns = [

    path('',include(router.urls)),
]