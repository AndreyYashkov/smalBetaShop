from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from sites.models import UserSite, SiteBlock
from sites.serializers import UserSiteSerializer, BlockSiteSerializer

from store.models import Products


class UserSiteViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = UserSite.objects.all()
    serializer_class = UserSiteSerializer
    lookup_field = "name"

    # @action(methods=["GET"], detail=True)
    # def catalog(self, request, *args, **kwargs):
    #     site = self.get_object()
    #     if not site.blocks.filter(block_type=SiteBlock.CATALOG_BLOCK):
    #         return Response(status=status.HTTP_404_NOT_FOUND)

