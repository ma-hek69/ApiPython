from rest_framework import viewsets
from .models import Product
from .models import Student
from .serializers import ProductSerializer
from .serializers import StudentSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Get all Product objects
    serializer_class = ProductSerializer  # Use the ProductSerializer for serialization
      
      
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
