from django.db import models
from api.users.models import User
import uuid
import os 
from django.conf import settings
from  django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

# Create agr model
# class  seller(models.Model):
#     pass



# class  Buyer(models.Model):
#     pass



class Product(models.Model):
    product_name = models.CharField( "library name",max_length=20,default="", blank=True)
    description = models.TextField("description_lib",default="", blank=True)
    category = models.CharField("cat", max_length=50, blank=True)
    quantity = models.IntegerField("qnt", default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # quality_check = models.ForeignKey("", verbose_name=_(""), on_delete=models.CASCADE)
    # logistic_details = models.ForeignKey("logistic", verbose_name=_("logistic name"), on_delete=models.CASCADE)  
    created_at = models.DateTimeField("create at ",auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.deletion.CASCADE, null=True)
    uuid = models.UUIDField("uuid", default=uuid.uuid4, editable=False)



    class Meta:
        db_table = "product_table"


# def upload_file_path_handler(instance, filename):
#     fn, ext = os.path.splitext(filename)

#     return "{files}/{uuid}/{ext}/{fname}".format(files=settings.ROOT_BOOK_DIR, uuid = instance.uuid, extension= ext, fname = filename)
def validator_file_size(fsize):
    limit_fs = 10 * 1024 * 1024
    if  fsize.size > limit_fs:
        raise ValidationError('File size should not exceed 10MB')
 


# def valid_filename(s):
#     file_n = File()
#     File_Name = file_n.file_upload.storage.generate_filename(s)
#     return File_Name

# class File (models.Model):
#     title = models.CharField(max_length=200,default="", blank=True)
#     author = models.CharField(max_length=100,default="", blank=True)
#     isbn = models.CharField(max_length=20 ,default="", blank=True)
#     summary = models.TextField()
#     # uuid = models.UUIDField("uuid", default=uuid.uuid4, editable=False)
#     file_name = models.CharField(max_length=100)
#     file_upload = models.FileField("upload_file",upload_to = upload_file_path_handler ,null=True,
#                                     blank=True,
#                                     validators=[FileExtensionValidator(["pdf","docx","txt", "xls", "xlsx",
#                                                     "ods", "doc", "odt", "ppt", "pptx"]),validator_file_size])
#     file_ext = models.CharField("extention", max_length=5,default="", blank=True)
#     file_sz = models.FloatField("file size", default=0)
#     create_at = models.DateTimeField("file_created",auto_now_add=True)
#     update_at = models.DateTimeField("file_updated",auto_now=True)
#     file_fk = models.ForeignKey(Product, on_delete=models.deletion.CASCADE, null = True)
#     genre = models.CharField(max_length=50,default="", blank=True)
#     available = models.BooleanField(default=True)
    
#     # def __str__(self):
#     #     return self.title
#     class Meta:
#         db_table = "onlib_file"

    
# class Authors(models.Model):
#     first_name = models.CharField("name", max_length=40)
#     uuid = models.UUIDField("uuid_author", default=uuid.uuid4, editable=True)
#     last_name = models.CharField("name", max_length=40)
#     email = models.EmailField("email", max_length=100, blank= True)
#     author_file = models.ForeignKey(File, on_delete=models.deletion.CASCADE, null= True)

#     class Meta:
#         db_table = "onlib_author"

# Create Borrow model
# class Borrow(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     borrow_date = models.DateTimeField(auto_now_add=True)
#     return_date = models.DateTimeField(null=True, blank=True)
#     def __str__(self):
#         return self.book.title
    

class Transaction(models.Model):
    pass

class Logistics(models.Model):
    pass

class Payment(models.Model):
    pass

class QualityCheck(models.Model):
    pass
