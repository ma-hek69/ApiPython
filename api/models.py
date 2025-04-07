from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    enrolled = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    
class FileUpload(models.Model):
    file = models.FileField(upload_to='uploads/')  # Indentation is important here
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File {self.file.name} uploaded at {self.uploaded_at}"
    
   