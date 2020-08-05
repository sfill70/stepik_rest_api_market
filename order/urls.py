from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import OrderViewSet


class OptionalSlashRouter(DefaultRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
router.register("orders", OrderViewSet, basename='orders')
urlpatterns = router.urls
