
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import MarketViewSet


class OptionalSlashRouter(DefaultRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register("product-sets", MarketViewSet, basename='product-sets')
urlpatterns = router.urls
