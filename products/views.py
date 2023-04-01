from rest_framework import generics
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Product
from .permissions import IsOwnerOrReadOnly
from .serializer import ProductSerializer, UserSerializer


class ViewProducts(generics.ListCreateAPIView, format=None):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ViewProductDetails(generics.RetrieveDestroyAPIView, format=None):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserList(generics.ListAPIView, format=None):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveDestroyAPIView, format=None):
    queryset = User.objects.all()
    serializer_class = UserSerializer
