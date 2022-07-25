from rest_framework import serializers

from sites.models import UserSite, SiteBlock
from users.serializers import UserSerializer


class UserSiteSerializer(serializers.ModelSerializer):
    user = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserSite
        fields = [
            "id",
            "name",
            "user",
        ]


class BlockSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteBlock
        fields = [
            "id",
            "block_type",
            "site"
        ]
