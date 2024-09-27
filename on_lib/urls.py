from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router_lib = DefaultRouter()
router_lib.register(r"books", views.BookAPIVIEW)



# Include the library API routes
urlpatterns = [
    path("", include(router_lib.urls)),  # Empty path since it's already prefixed in the main urls.py
]