from rest_framework import viewsets, mixins
# from rest_framework.permissions import AllowAny
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# from .models import User
# from rest_framework.permissions import IsAuthenticated
# from .permissions import 
# from .serializers import CreateUserSerializer, UserSerializer, ChangePasswordSerializer
from .models  import Product, Logistics, Rdv
from .serializers import ProductSerializer, LogisticSerialize, RdvSerializer
from .paginations import CustomPageNumberPagination
from .permission import Has_permissionOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Q

class ProductAPIVIEW(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    
    queryset=Product.objects.all()
    # queryset=Book.objects.get(title="j")
    serializer_class = ProductSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (Has_permissionOrReadOnly, IsAuthenticated)
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # filterset_fields = [
    #     "title",
    #     "author",
    # ]
    # search_fields = ["title", "summary"]


    ordering_fields = "__all__"

    def get_queryset(self):
        return super().get_queryset()
    def  create(self, request, *args, **kwargs):
        request.data._mutable = True 
        request.data["owner"] = request.user.id
        request.data._mutable = False 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().create(request, *args, **kwargs)
    


class LogisticAPIVIEW(mixins.RetrieveModelMixin,

                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    
    queryset=Logistics.objects.all()
    serializer_class = LogisticSerialize
    # pagination_class = CustomPageNumberPagination
    permission_classes = (Has_permissionOrReadOnly, IsAuthenticated)
    
    
    def get_queryset(self):
        return super().get_queryset()
    def  create(self, request, *args, **kwargs):
        request.data._mutable = True 
        request.data["owner"] = request.user.id
        request.data._mutable = False 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().create(request, *args, **kwargs)
    
    

    # def create(self, request, *args, **kwargs):
    #     data = request.data.copy()
    #     data["owner"] = request.user.id
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     return super().create(request, *args, **kwargs)
    # def create(self, request, *args, **kwargs):
        # return super().create(request, *args, **kwargs)
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    


    
class RdvAPIVIEW(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    
    queryset=Logistics.objects.all()
    serializer_class = RdvSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (Has_permissionOrReadOnly, IsAuthenticated)
    
    
    def get_queryset(self):
        return super().get_queryset()
    def  create(self, request, *args, **kwargs):
        request.data._mutable = True 
        request.data["owner"] = request.user.id
        request.data._mutable = False 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().create(request, *args, **kwargs)