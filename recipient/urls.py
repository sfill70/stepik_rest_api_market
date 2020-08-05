from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import RecipientsViewSet


class OptionalSlashRouter(DefaultRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()
# router = SimpleRouter(trailing_slash=False)
router.register("recipients", RecipientsViewSet, basename='recipient')
urlpatterns = router.urls
