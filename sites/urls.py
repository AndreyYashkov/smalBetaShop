from rest_framework.routers import DefaultRouter

from sites.views import UserSiteViewSet


router = DefaultRouter()
router.register("domains", UserSiteViewSet)

urlpatterns = router.urls
