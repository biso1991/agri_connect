from .models import Book_project_lib
from rest_framework import serializers

# serializing book and borrow
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book_project_lib
        fields = '__all__'


class GetBookByUserSerialize(serializers.Serializer):

    owner = serializers.CharField(required=True)




























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
