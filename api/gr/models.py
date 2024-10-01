from django.db import models
from api.users.models import User
import uuid
import os 
from django.conf import settings
from  django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import enum

# Create agr model



    
# class rate(enum.Enum): 
#     Poor = 1
#     Fair = 2
#     Good = 3
#     Very_Good = 4 
#     Excellent = 5



    # PRIVATE = 0
    # PUBLIC = 1
    # scope_choices = (
    #     (PRIVATE, "Private"),
    #     (PUBLIC, "Public"),
    # )



class Product(models.Model):
    product_name = models.CharField( "library name",max_length=20,default="", blank=True)
    description = models.TextField("description_lib",default="", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null= True)
    # option = models.CharField("option quantity", max_length=50, choices=Choose_opt_Prod, default=Choose_opt_Prod.SINGLE_PROD.value)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # quality_check = models.ForeignKey("", verbose_name=_(""), on_delete=models.CASCADE)
    # logistic_details = models.ForeignKey("logistic", verbose_name=_("logistic name"), on_delete=models.CASCADE)  
    created_at = models.DateTimeField("create at ",auto_now_add=True)
    stock = models.IntegerField("stock", default=0)
    type = models.CharField("Type of product", max_length=20)
    # warranty = models.CharField("warranty of product", max_length=50) important
    # rating = models.FloatField(" rating of  product", choices=) check with rate class 
    owner = models.ForeignKey(User, on_delete=models.deletion.CASCADE, null=True)
    uuid = models.UUIDField("uuid", default=uuid.uuid4, editable=False)

    class Meta:
        db_table = "product_table"
class Category(models.Model):
    name = models.CharField(max_length=50)
    uuid = models.UUIDField("uuid", default=uuid.uuid4, editable=False )

    product_k = models.ForeignKey(Product, on_delete=models.CASCADE, null = True) 
class Consumer(models.Model):
    # name = models.CharField("name", max_length=20, default="", blank=True)
    # email = models.EmailField("email", max_length=50, default="", blank=True)
    # #get address 
    # address = models.CharField("address", max_length=50, default="", blank=True)
    #get phone number
    phone_number = models.CharField("phone number", max_length=20, default="", blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null = True )
    uuid = models.UUIDField("uuid", default=uuid.uuid4, editable=False)
    class Meta:
        db_table = "consumer_table"

class Status(enum.Enum):
    IDLE = "idle"
    PENDING = "pending"
    DELIVERED = "delivered"
    CANCELED = "canceled"
    # BIKE = "bike"
class Order(models.Model):
    # get order date
    order_date = models.DateTimeField("order date", auto_now_add=True)
    # get order status
    status = models.CharField("status",  choices= Status, default=Status.IDLE.value)
    # get order items
    # order_items = models.ForeignKey(order_item, on_delete=models.CASCADE, null = True)
    # get consumer
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, null = True)
    # get total price
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # h!!!!!!!!!!!!!!
    # get payment method

class Payment_type(enum.Enum):
    CASH = "cash"
    CARD = "card"
    RIP = "Rip"
    # BIKE = "bike"

class Choose_opt_Prod(enum.Enum):
    """Enum for choose opt prod"""
    GROUP_PROD = 1
    SCOUP_CHOICE = "Group product"
                    
    


class Payment(models.Model):
    payment_method = models.CharField("payment method", max_length=20,choices=Payment_type ,
                                      default=Payment_type.CASH.value, blank=True)
    # get order
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    # get amount
    singel_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    group_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0,choices=Choose_opt_Prod.SCOUP_CHOICE)
    # get owner
    owner = models.ForeignKey(User, on_delete=models.CASCADE,null = True )
    uuid = models.UUIDField("uuid", default=uuid.uuid4, editable=False)

         
class Order_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # item_name = models.CharField("item name", max_length=20, default="", blank=True)
    quantity = models.IntegerField("qnt", default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    uuid  = models.UUIDField("uuid", default=uuid.uuid4, editable=False)
    owner =  models.ForeignKey(User, on_delete=models.deletion.CASCADE, null=True)
    item_K = models.ForeignKey(Order, on_delete=models.CASCADE, null = True)



# # get transportMode  mode choice 
# class TransportMode(enum.Enum):
#     POST = "post"
#     CAR = "car"
#     # BIKE = "bike"
# # get delivery_Status  mode choice    
# class Status(enum.Enum):
#     IDLE = "idle"
#     PENDING = "pending"
#     DELIVERED = "delivered"
#     CANCELED = "canceled"
#     # BIKE = "bike"



# class Location(enum.Enum):
#     MEDJAZ_BAB = "Medjaz_El_Bab"
#     TUNIS = "Tunis"
#     ARIANA = "Ariana"
    # BEN_AROUS = "Ben Arous"
    # BEJA = "Beja"
    # BIZERT = "Bizert"
    # GABES = "Gabes"
    # NABEL = "Nabel"
    # MANOUBA = "Manouba"
    # MEDENINE = "Medenine"
    # MONASTIR = "Monastir"
    # SFAX = "Sfax"
    # SIDI_BOUZID = "Sidi Bouzid"
    # SILIANA = "Silia"
    # Sousse = "Sousse"
    # TOZEUR = "Tozeur"
    # TATAOUINE = "Tataouine"
    # ZAGHOUAN = "Zaghouan"
    # KASSERINE = "Kasserine"
    # KBELI = "Kbeli"
    # KAFSA = "Kafsa"
    # KAIROUAN = "Kairouan"
    # GAFSA = "Gafsa"
    # JENDOUBA = "Jandouba"
    # KEF = "Kef"
    # MAHDIA = "Mahdia"

class Logistics(models.Model):
    choice_delivery = ((Status.IDLE.value, "idle"),
                       (Status.PENDING.value, "pending"),
                       (Status.DELIVERED.value, "delivered"),
                       (Status.CANCELED.value, "canceled")
                       )
    choices_mode = ((TransportMode.POST.value ,"post"),
                   (TransportMode.CAR.value, "car")
                   )
    owner = models.ForeignKey(User, on_delete=models.deletion.CASCADE, null=True)
    uuid = models.UUIDField("uuid", default=uuid.uuid4, editable=False)
    transportMode = models.CharField("transportM", choices=choices_mode, default=TransportMode.CAR.value, max_length=40)
    deliveryStatus = models.CharField("deliveryStatus", choices= choice_delivery, default=Status.IDLE.value,max_length=40) 
    shippingDetails =  models.CharField("shippingDetails", max_length=50)
    product_log = models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        db_table = "logistic_table"

# def upload_file_path_handler(instance, filename):
#     fn, ext = os.path.splitext(filename)

#     return "{files}/{uuid}/{ext}/{fname}".format(files=settings.ROOT_BOOK_DIR, uuid = instance.uuid, extension= ext, fname = filename)
def validator_file_size(fsize):
    limit_fs = 10 * 1024 * 1024
    if  fsize.size > limit_fs:
        raise ValidationError('File size should not exceed 10MB')
 
class Contact_method(enum.Enum):
    LOCATION = "In person"
    ONLINE = "Online Meeting"
    PHONE = "Phone Call"

class Status(enum.Enum):
    SCHEDULED = "Scheduled"
    CANCELED = "Canceled"

    
    
class  Rdv(models.Model):
    choice_location = ((Contact_method.LOCATION.value, "In person"),
                       (Contact_method.ONLINE.value, "Online Meeting"),
                       (Contact_method.PHONE.value, "Phone Call")
                       )                
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    uuid = models.UUIDField("uuid", default=uuid.uuid4, editable=False)
    # location = models.CharField("loca_tion", choices=choice_location, default=Location.MEDJAZ_BAB.value, max_length=40)
    product_loc = models.ForeignKey(Product,  on_delete=models.CASCADE , null = True)
    date = models.DateField("created at", auto_now_add=True)
    time = models.TimeField("created at", auto_now_add=True)
    type = models.CharField("type", max_length=15, choices=choice_location, default=Contact_method.PHONE.value)
    status = models.CharField(max_length=20, default='Scheduled')
    class Meta:
        db_table = "rdv_table"
        # ordering = ["-date", "-time"]
    # you can add a graphical Map here

# class Client(models.Model):
#     choice_location = ((Location..value, "In Person"),
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     preferred_method = models.CharField(
#         max_length=10,
#         choices=[('location', 'In Person'), ('online', 'Online Meeting'), ('phone', 'Phone Call')],
#         default='location'
#     )
#     location = models.CharField(max_length=200, blank=True, null=True)

#     def __str__(self):
#         return self.name

# class RDV(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     date = models.DateField()
#     time = models.TimeField()
#     type = models.CharField(
#         max_length=10,
#         choices=[('location', 'In Person'), ('online', 'Online Meeting'), ('phone', 'Phone Call')],
#     )
#     status = models.CharField(max_length=20, default='Scheduled')

#     def __str__(self):
#         return f"{self.client.name} - {self.date} at {self.time} ({self.type})"

#########################################################################################################""""""
# check layer 
# class MeetingPlatform(models.Model):
#     platform_name = models.CharField(max_length=50, default='Zoom')
#     meeting_link = models.URLField(max_length=200, blank=True, null=True)

#     def __str__(self):
#         return self.platform_name

class Location(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.address


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
    

# class Transaction(models.Model):
#     pass

# class Logistics(models.Model):
#     pass

# class Payment(models.Model):
#     pass

# class QualityCheck(models.Model):
#     pass
