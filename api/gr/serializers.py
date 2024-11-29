from .models import Product, Market 
from rest_framework import serializers

# serializing book and borrow

# class Market Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Market 
#         fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Product
#         fields = '__all__'

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market 
        fields = '__all__'

class GetProductByUserSerialize(serializers.Serializer):

    owner = serializers.CharField(required=True)

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AdminProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'description',"rating", ]  # Basic fields

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



# class LogisticSerialize(serializers.ModelSerializer):
#       class Meta:
#         model = Logistics
#         fields = '__all__'
# class RdvSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = Rdv
#         fields= "__all__"
# class 





























#################################################################################################################
# class BookSerializer(serializers.ModelField):
#     title = serializers.SerializerMethodField()
#     author =serializers.SerializerMethodField()
#     isbn = serializers.SerializerMethodField()
#     summary = serializers.SerializerMethodField()
#     genre = serializers.SerializerMethodField()
#     available = serializers.SerializerMethodField()
#     created_at = serializers.SerializerMethodField()
#     updated_at = serializers.SerializerMethodField()

# class BorrowSerilizers(serializers.ModelField):
#     id = serializers.SerializerMethodField()
#     book = serializers.SerializerMethodField()
#     borrower = serializers.SerializerMethodField()
#     borrow_date = serializers.SerializerMethodField()
#     return_date = serializers.SerializerMethodField()
#     created_at = serializers.SerializerMethodField()
#     updated_at = serializers.SerializerMethodField()
#     status = serializers.SerializerMethodField()
#     fine = serializers.SerializerMethodField()
#     fine_amount = serializers.SerializerMethodField()
#     fine_status = serializers.SerializerMethodField()
#     fine_date = serializers.SerializerMethodField()
#     fine_amount_paid = serializers.SerializerMethodField()
