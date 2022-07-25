from django.db import models


class UserSite(models.Model):
    name = models.CharField(max_length=25, unique=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="sites")

    def __str__(self):
        return f"<Site {self.id} {self.name}>"


class SiteBlock(models.Model):
    AUTH_BLOCK = 1
    CATALOG_BLOCK = 2
    CONTACTS_BLOCK = 3

    BLOCK_CHOICES = (
        (AUTH_BLOCK, "Authorization"),
        (CATALOG_BLOCK, "Catalog"),
        (CONTACTS_BLOCK, "Contacts"),
    )

    block_type = models.SmallIntegerField(choices=BLOCK_CHOICES)
    site = models.ForeignKey("sites.UserSite", on_delete=models.CASCADE, related_name="blocks")

    def __str__(self):
        return f"<SiteBlock {self.id} {self.block_type} {self.site}>"

    class Meta:
        unique_together = ["block_type", "site"]
