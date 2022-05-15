from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path("api/profile/", include("apps.profiles.urls")),
    path("api/properties/", include("apps.properties.urls")),
    path("api/ratings/", include("apps.ratings.urls")),
    path("api/queries/", include("apps.queries.urls")),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="docs",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Portal"
admin.site.index_title = "Welcome to Real Estate Admin Portal"
