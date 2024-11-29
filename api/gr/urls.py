from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router_lib = DefaultRouter()
router_lib.register(r"product", views.ProductAPIVIEW )
router_lib.register(r"Market", views.MarketAPIView)


#  views.ConsumerSerializer,

# Include the library API routes
# Empty path since it's already prefixed in the main urls.py
urlpatterns = [
    path("prd/", include(router_lib.urls)),
    # view Market apiview
    path('Mark/', include(router_lib.urls)),
    # path('Market', include())fùg;g,
]