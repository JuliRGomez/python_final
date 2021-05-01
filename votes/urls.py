from rest_framework.routers import DefaultRouter
from votes.views import VotesViewSet

router = DefaultRouter()
router.register(r'votes', VotesViewSet)

urlpatterns = router.urls
