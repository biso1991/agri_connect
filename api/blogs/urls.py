# from django.urls import path
# from .views import blogdeco
# # from rest_framework.routers import DefaultRouter
# from django.contrib import admin

# # router_lib = DefaultRouter()
# # router_lib.register(r"Blogdeco", views.blogdeco )


# #  views.ConsumerSerializer,

# # Include the library API routes
# # Empty path since it's already prefixed in the main urls.py
# urlpatterns = ([
#     # path("admin/", admin.site.urls),  # Ensure this line is correct
#     path("blog/", blogdeco),
#     # path("blogs/", include(router_lib.urls)),
#     # path('Market', include())fùg;g,
# ])
from django.urls import path
from .views import blogdeco

urlpatterns = [
    path("", blogdeco),
]