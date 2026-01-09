from django.urls import path
from .views import (
    CarListCreateAPIView,
    CarRetrieveUpdateDestroyAPIView,
    CarListByChildCategorySlugAPIView,
)

urlpatterns = [
    path('cars/', CarListCreateAPIView.as_view()),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view()),
    path('cars/by-category/<slug:slug>/', CarListByChildCategorySlugAPIView.as_view()),
]
