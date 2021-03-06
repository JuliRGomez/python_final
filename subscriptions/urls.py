from rest_framework.routers import DefaultRouter
from subscriptions.views import SubscriptionViewSet

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = router.urls
