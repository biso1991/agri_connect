from rest_framework import viewsets, mixins
# from rest_framework.permissions import AllowAny
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# from .models import User
# from rest_framework.permissions import IsAuthenticated
# from .permissions import 
# from .serializers import CreateUserSerializer, UserSerializer, ChangePasswordSerializer
from .models  import Product,Market
from .serializers import ProductSerializer,MarketSerializer,ConsumerSerializer
from .paginations import CustomPageNumberPagination
from .permission import Has_permissionOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Q
from rest_framework import status

class MarketAPIView(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = Market.objects.all()
    # print queryset data object 


    serializer_class = MarketSerializer
    # print(serializer_class,"##############################################")

    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data, "##################################")
        
        # if serializer.is_valid():
        #     market_id = request.data.get("mark_number")  # Adjusted key to match request data
        #     if not market_id:
        #         return Response(
        #             {"message": "Market ID not provided"},
        #             status=status.HTTP_400_BAD_REQUEST
        #         )
        #     try:
        #         # Ensure market_id is an integer
        #         market_id = int(market_id)
        #         prod = Market.objects.get(id=market_id)
        #     except ValueError:
        #         return Response(
        #             {"message": "Market ID must be an integer"},
        #             status=status.HTTP_400_BAD_REQUEST
        #         )
        #     except Market.DoesNotExist:
        #         return Response(
        #             {"message": "No Market found"},
        #             status=status.HTTP_404_NOT_FOUND
        #         )
        # else:
        #     return Response(
        #         serializer.errors,
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
        # mrt = Market.objects.all()
        # print(mrt, "######################################55555")
        return super().create(request, *args, **kwargs)

# class MarketAPIView(mixins.CreateModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.ListModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     viewsets.GenericViewSet,
#                   ):
#     # get format get method 
#     # queryset = Market.objects.get()

#     queryset = Market.objects.all()
#     serializer_class = MarketSerializer
#     def create(self, request, *args, **kwargs):
#         serializer_class = MarketSerializer
#         print(serializer_class)
#         if serializer_class.is_valid():
#            try:
#                 prod = Market.objects.get(id=request.data.get("market_k"))
#            except:
#                 return Response(
#                     {
#                         "message": "No Manket found"
#                     },
#                         status=status.HTTP_404_NOT_FOUND
#                 )
#         mrt = Market.objects.all()
#         print(mrt, "######################################55555")
#         serializer_class = self.get_serializer(data=request.data)      
#         # print(request.data)
#     #    print("##################################")
#     #    prod = Market.objects.get(id=request.data.get("market_k"))
#     #    print(prod)
#         return super().create(request, *args, **kwargs)
    
#     def get_queryset(self):
#        return super().get_queryset()
   
    
    
    # permission_classes = [Has_permissionOrReadOnly,IsAuthenticated]
       # filter_backends = [DjangoFilterBackend,filters.SearchFilter]
       # search_fields = ['name']
       # pagination_class = CustomPageNumberPagination
       # filter_fields = ['name']
    # # get Market by pruduct owner 
    # def get_queryset(self):
    # #    product_k = ()
    # #    for product in  Product.objects.all().filter(owner=self.request.data)
    #    return super().get_queryset()
   
   
        
    # def get_queryset(self):
    #     return super().get_queryset()
    #  # post market

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     # print ("#######################################################")
    #     # print(request.user, request.get())
    #     request.data._mutable = True 
    #     request.data["owner"]=request.user.id
    #     request.data._mutable = False 
    #     serializer = self.get_serializer(data=request.data)
    #     print(request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return super().create(request, *args, **kwargs)





class ProductAPIVIEW(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    
    queryset=Product.objects.all()
    # for item in queryset:
    #     print(item.product_name)
    # print all queryset
    # print(queryset)
    # queryset=Book.objects.get(title="j")
    serializer_class = ProductSerializer
    print(serializer_class)

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer(data=request.data)
        # mr = Market.objects.get(id=1)
        # print(mr.name, "##################################################")
        # if serializer_class.is_valid():
        #     try:
        #         makeret_id = Market.objects.get(
        #             id=serializer_class.validated_data["Market"].id
        #         )
        #     except:
        #         return Response(
        #             {"message": "No MARKET  found"}, status=status.HTTP_404_NOT_FOUND
                # )
        print(request.data, "####################")
        request.data._mutable =True
        request.data["owner"]=request.user.id
        request.data._mutable = False
        print(request.data," ééééééééééééééééééééééééééééé")
        # if serializer_class.is_valid():
        #     # mk = Market.objects.get(id= request.data("market_k"))
        #     print(request.data)
        #     print(len(request.data))
        # else:
        #     print("mark is not found")
        return super().create(request, *args, **kwargs)
        # if serializer.is_valid():
        #     try:
        #         ownerProject = Project.objects.get(
        #             id=serializer.validated_data["project"].id
        #         )
        #     except:
        #         return Response(
        #             {"message": "No project found"}, status=status.HTTP_404_NOT_FOUND
        #         )
        #     permission = Has_permissionOrReadOnly.has_object_permission(
        #         self, request, None, ownerProject
        #     )
        #     if permission == True:
        #         ownerProject.files_hash = get_hash(ownerProject)
        #         ownerProject.save()
        #         serializer.save()
        #         response = {"data": serializer.data, "status": "success"}
        #         return Response(response, status=status.HTTP_201_CREATED)
        #     else:
        #         response = {
        #             "message": "You don't have permission to access this resource",
        #             "status": "error",
        #         }
        #         return Response(response, status=status.HTTP_403_FORBIDDEN)
        # else:
        #     response = {"message": serializer.errors, "status": "error"}
        #     return Response(response, status=status.HTTP_400_BAD_REQUEST) 
        # serializer.is_valid(raise_exception=True)
        # headers = self.get_success_headers(serializer.data)
        # print(request.data)
        
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # def create(self, request, *args, **kwargs):
    #     serializer_class = ProductSerializer(data = request.data)
        # request.data._mutable = True 
        # request.data["owner"] = request.user.id
        # request.data._mutable = False 
        # print(request.data)
        # if 

        #  {'product_name': ['bnff'], 'description': ['erbreb'], 'price': ['55.5'], 'stock': [''], 'rating': [''], 'type': [''], '': ['']}>

        # if serializer_class.is_valid():
        # market_k = Product.objects.get(market_k = request.data)
        # we need to set a custom id market  in  product table  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # print(market_k)
        # return super().create(request, *args, **kwargs)
    
    # {'product_name': ['bnff'], 'description': ['erbreb'], 'price': ['55.5'], 'stock': [''], 'rating': [''], 'type': [''], '': [''], 'owner': [UUID('8ce8a880-e844-4078-ac38-6ee29b21b1cc')]}>

        # if serializer.is_valid():
        #     market_k = Market.objects.get(id=request.data.get("market_k"))
        #     serializer.save(market_k=market_k)
        #     print(serializer.save)
        # else:
        #    return Response(
        #             {"message": "You don't have permission to access this resource"},
        #             status=status.HTTP_403_FORBIDDEN,
        #         )
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    # def get_serializer_class(self):
    #     # Use AdminProductSerializer if the user is an admin
    #     if self.request.user.is_staff:
    #         return AdminProductSerializer
        # Otherwise, use the regular ProductSerializer
        # return ProductSerializer

    def get(self, request, *args, **kwargs):
        # Fetch all products and serialize based on the user type
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        # print(serializer_class)
        # print("##########################")
        # if serializer_class.is_valid():
        #     try:

    # pagination_class = CustomPageNumberPagination
    # permission_classes = (Has_permissionOrReadOnly, IsAuthenticated)
        # return super().create(request, *args, **kwargs)
    
    # filter_backends = [
    #     DjangoFilterBackend,
    #     filters.SearchFilter,
    #     filters.OrderingFilter,
    # ]
    # filterset_fields = [
    #     "title",
    #     "author",
    # ]
    # search_fields = ["title", "summary"]


    # ordering_fields = "__all__"
# Request parsing:
    # .data, .query_params, .parser
# Authentication:
    # .user, .auth, .authenticators    
    # def get_queryset(self):
    #     return super().get_queryset()
    
    #  def create(self, request, *args, **kwargs):
    #     serializer = MultiFileSerialize(data=request.data)
    #     print(request.data)
    #     response = {}
    #     if serializer.is_valid():
    #         try:
    #             project = Project.objects.get(id=request.data.get("project_f"))
    #             print(request.data.get("project_f"))
    #         except:
    #             return Response(
    #                 {"message": "No project found"}, status=status.HTTP_404_NOT_FOUND
    #             )
    #         if Has_permissionOrReadOnly.has_object_permission(self, request, None, project):
    #             for file in serializer.validated_data["file_f"]:
    #                 exists_f = File.objects.filter(file_name=valid_filename(file.name), project_f=project)
    #                 print(exists_f)
    #                 if len(exists_f) == 0:
    #                     data = {
    #                         "file_f": file,
    #                         "project_f": serializer.validated_data["project_f"],
    #                     }
    #                     serializer_SingleFile = FileSerialize(data=data)
    #                     print(serializer_SingleFile)
    #                     if serializer_SingleFile.is_valid():
    #                         serializer_SingleFile.save()
    #                         response[file.name] = {
    #                             "data": serializer_SingleFile.data,
    #                             "status": "success",
    #                         }
    #                     else:
    #                         response[file.name] = {
    #                             "data": serializer_SingleFile.errors,
    #                             "status": "error",
    #                         }
    #             return Response(response, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(
    #                 {"message": "You don't have permission to access this resource"},
    #                 status=status.HTTP_403_FORBIDDEN,
    #             )
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
        # if serializer.is_valid():
            

        # print(request.user)
        # if serializer.is_valid():
        #     # try:
        #         ownerMarket = Market.objects.get(
        #         id=serializer.validated_data["name"].id
        #         print(id)
            # {'product_name': ['bnff'], 'description': ['erbreb'], 'category': ['errbeeffff'], 'price': ['55.5'], 'stock': [''], 'rating': ['']}>
  
            # 
            # 
            # 
            #   )
            # except:
            #     return Response(
            #         {"message": "No project found"}, status=status.HTTP_404_NOT_FOUND
                # )
            # permission = Has_permissionOrReadOnly.has_object_permission(
            #     self, request, None, ownerProject
            # )
        #     if permission == True:
        #         ownerProject.files_hash = get_hash(ownerProject)
        #         ownerProject.save()
        #         serializer.save()
        #         response = {"data": serializer.data, "status": "success"}
        #         return Response(response, status=status.HTTP_201_CREATED)
        #     else:
        #         response = {
        #             "message": "You don't have permission to access this resource",
        #             "status": "error",
        #         }
        #         return Response(response, status=status.HTTP_403_FORBIDDEN)
        # else:
        #     response = {"message": serializer.errors, "status": "error"}
            # return Response(response, status=status.HTTP_400_BAD_REQUEST)

        # print(data)
        # serializer.is_valid(raise_exception=True)
        # print(serializer.data, "this is #################################################################################")
########################################################################################################################################
# def create(self, request, *args, **kwargs):
#         serializer = MultiFileSerialize(data=request.data)
#         response = {}  # list !!!!!!
#         if serializer.is_valid():
#             try:
#                 project = Project.objects.get(id=request.data.get("project_f"))
#             except:
#                 return Response(
#                     {"message": "No project found"}, status=status.HTTP_404_NOT_FOUND
#                 )
#             if Has_permissionOrReadOnly.has_object_permission(
#                 self, request, None, project
#             ):
#                 for file in serializer.validated_data["file_f"]:
#                     exists_f = File.objects.filter(
#                         file_name=valid_filename(file.name), project_f=project
#                     )
#                     if len(exists_f) == 0: # empty response list: {} we need to check list !!!!!! or append list
#                         data = {
#                             "file_f": file,
#                             "project_f": serializer.validated_data["project_f"],
#                         }
#                         serializer_SingleFile = FileSerialize(data=data)
#                         if serializer_SingleFile.is_valid():
#                             serializer_SingleFile.save()
#                             response[file.name] = {
#                                 "data": serializer_SingleFile.data,
#                                 "status": "success",
#                             }
#                         else:
#                             response[file.name] = {
#                                 "data": serializer_SingleFile.errors,
#                                 "status": "error",
#                             }
#                 return Response(response, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(
#                     {"message": "You don't have permission to access this resource"},
#                     status=status.HTTP_403_FORBIDDEN,
#                 )
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#######################################################################################################################################""



# class CustomerAPIView(mixins.RetrieveModelMixin,
#                   mixins.ListModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.CreateModelMixin,
#                   viewsets.GenericViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
    # permission_classes = [Has_permissionOrReadOnly,IsAuthenticated]
    # filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # search_fields = ['name']
    # pagination_class = CustomPageNumberPagination
    # filter_fields = ['name']


# class LogisticAPIVIEW(mixins.RetrieveModelMixin,

#                   mixins.ListModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.CreateModelMixin,
#                   viewsets.GenericViewSet):
    
#     queryset=Logistics.objects.all()
#     serializer_class = LogisticSerialize
#     # pagination_class = CustomPageNumberPagination
#     permission_classes = (Has_permissionOrReadOnly, IsAuthenticated)
    
    
#     def get_queryset(self):
#         return super().get_queryset()
#     def  create(self, request, *args, **kwargs):
#         request.data._mutable = True 
#         request.data["owner"] = request.user.id
#         request.data._mutable = False 
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return super().create(request, *args, **kwargs)
    
    

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
    


    
# class RdvAPIVIEW(mixins.RetrieveModelMixin,
#                   mixins.ListModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.CreateModelMixin,
#                   viewsets.GenericViewSet):
    
#     queryset=Logistics.objects.all()
#     serializer_class = RdvSerializer
#     # pagination_class = CustomPageNumberPagination
#     permission_classes = (Has_permissionOrReadOnly, IsAuthenticated)
    
    
#     def get_queryset(self):
#         return super().get_queryset()
#     def  create(self, request, *args, **kwargs):
#         request.data._mutable = True 
#         request.data["owner"] = request.user.id
#         request.data._mutable = False 
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return super().create(request, *args, **kwargs)