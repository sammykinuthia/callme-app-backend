from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ViewProducts, ViewProductDetails, UserList, UserDetails

urlpatterns = [
    path('products/', ViewProducts.as_view(), name='products'),
    path('products/<int:pk>/', ViewProductDetails.as_view(), name='product'),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetails.as_view()),

    path('api-auth/', include('rest_framework.urls')),#api login


    # path('products/<int:id>/',ViewProduct.as_view(), name='product'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
