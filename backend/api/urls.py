from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r"products", ProductViewset)

urlpatterns = [
    path("import/", import_data, name="import-product"),
    path("", include(router.urls))
]