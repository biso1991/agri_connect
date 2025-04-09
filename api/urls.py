# # from django.contrib import admin
# from django.urls import path, re_path, include, reverse_lazy
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.generic.base import RedirectView
# from rest_framework.routers import DefaultRouter
# from .users.views import UserViewSet, UserCreateViewSet, UserAuthToken
# from api.gr.urls import router_lib

# from django.contrib import admin

# router = DefaultRouter()
# router.register(r"users", UserViewSet)
# router.register(r"users", UserCreateViewSet)

# urlpatterns = (
#     [
#         path("admin/", admin.site.urls),  # admin url
#         path("api/v1/", include(router.urls)),  # api root url
#         path("api/v1/agr/", include(router_lib.urls)),  # api entity url
#         path('api-token-auth/', UserAuthToken.as_view(), name='api_token_auth'),
#         path('api/v1/agr/blog/', include(blogs.urls)),  # Corrected blogs.urls import
#         path(
#             "api/password_reset/",
#             include("django_rest_passwordreset.urls", namespace="password_reset"),
#         ),
#         re_path(
#             r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)
#         ),
#     ]
#     + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# )


from django.urls import path, re_path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from .users.views import UserViewSet, UserCreateViewSet, UserAuthToken
from api.gr.urls import router_lib
from django.contrib import admin

# Correct import for blogs.urls
import api.blogs.urls as blogs_urls

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"users", UserCreateViewSet)

urlpatterns = (
    [
        path("admin", admin.site.urls),  # admin url
        path("api/v1/", include(router.urls)),  # api root url
        path("api/v1/agr/", include(router_lib.urls)),  # api entity url
        path('api-token-auth/', UserAuthToken.as_view(), name='api_token_auth'),
        path('api/v1/agr/blog/', include(blogs_urls)),  # Corrected blogs.urls import
        path(
            "api/password_reset/",
            include("django_rest_passwordreset.urls", namespace="password_reset"),
        ),
        re_path(
            r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)