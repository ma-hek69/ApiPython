from rest_framework import viewsets
from .models import Product
from .models import Student
from .serializers import ProductSerializer
from .serializers import StudentSerializer
from .models import FileUpload
from .serializers import FileUploadSerializer
from django.shortcuts import render


def form_view(request):
    return render(request, 'form.html')

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Get all Product objects
    serializer_class = ProductSerializer  # Use the ProductSerializer for serialization
      
      
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()  # Get all FileUpload objects
    serializer_class = FileUploadSerializer  # Use the FileUploadSerializer for serialization