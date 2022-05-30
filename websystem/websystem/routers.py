from book.views import AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter
from users.urls import urlpatterns as userurlpatterns

router = DefaultRouter()
router.register(r"book", BookViewSet, basename="Book")
router.register(r"author", AuthorViewSet, basename="Author")
app_name = "api"
urlpatterns = router.urls + userurlpatterns
print("url_pattenrs : ", urlpatterns)
