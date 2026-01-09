from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import Car, Category
from .serializers import CarSerializer


class CarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarListByChildCategorySlugAPIView(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')

        try:
            category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise NotFound("Category not found")

        if category.parent is None:
            raise NotFound("This is not a child category")

        return Car.objects.filter(category=category)
