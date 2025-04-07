# api/urls.py
from django.urls import path, include
from .views import form_view 
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StudentViewSet, FileUploadViewSet, form_view    

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'students', StudentViewSet)
router.register(r'file-upload', FileUploadViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('form/', form_view, name='form'), 
    
]
