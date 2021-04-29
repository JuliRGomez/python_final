from rest_framework.routers import DefaultRouter

from newsletters.views import NewsletterViewSet

router = DefaultRouter()
router.register(r'', NewsletterViewSet)

urlpatterns = router.urls
