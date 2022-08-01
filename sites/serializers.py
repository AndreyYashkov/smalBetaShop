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
    def create(self, validated_data):
        site_data = validated_data.pop('name')
        user = User.objects.create(**validated_data)
        UserSite.objects.create(user=user, **site_data)
        return user


class BlockSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteBlock
        fields = [
            "id",
            "block_type",
            "site"
        ]
