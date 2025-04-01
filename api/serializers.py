from rest_framework import serializers
from .models import Product
from .models import Student
from .models import FileUpload

# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # This includes all the fields from the Product model

# Serializer for Student model
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# Serializer for FileUpload model (should be defined outside of the StudentSerializer)
class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = '__all__'
