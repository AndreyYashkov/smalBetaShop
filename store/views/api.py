from rest_framework import viewsets

from store.models import Products
from store.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.select_related("site")
    serializer_class = ProductSerializer
    lookup_field = "name"

    def get_queryset(self):
        domain_name = self.kwargs["domain_name"]
        queryset = self.queryset.filter(site__name=domain_name)
        return queryset
