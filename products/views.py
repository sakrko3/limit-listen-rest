from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.permissions import AdminAllManagerAllExceptCreateStaffView
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AdminAllManagerAllExceptCreateStaffView and IsAuthenticated]
