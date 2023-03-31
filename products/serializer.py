from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.views import APIView
from .models import Category, Product


class UserSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    class Meta:
        model = User
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'username', 'product', 'owner']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')
    # name = serializers.CharField(max_length=200)
    # description = serializers.CharField()
    # category = Category()
    # price  = serializers.DecimalField(max_digits=10, decimal_places=2)
    # image = serializers.ImageField()
    # owner = get_user_model()
