from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .seed_data import seed_data
from django.http import JsonResponse
# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer

def import_data(request):
    for data in seed_data:
        product = Product(
            name = data['name'],
            description = data['description'],
            os = data['os'],
            quantity = data['quantity'],
            price = data['price'],
        )

        product.save()

    message = {
        "message": "Seed Data imported Successfully"
    }

    return JsonResponse(message)