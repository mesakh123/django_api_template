from book.views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"books", BookViewSet)

app_name = "api"
urlpatterns = router.urls
