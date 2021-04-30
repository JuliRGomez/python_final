from rest_framework.routers import DefaultRouter
from users.views import UsersViewSet, UsersAdminView

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'users-admin', UsersAdminView)

urlpatterns = router.urls
