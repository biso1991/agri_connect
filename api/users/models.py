import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
import enum


# def check_country_nm(country_number): cheking !!!!!! 
    # user =User.objects.get(country=instance.country_nm)
    # return "{country_number}".format(country_number="+216")


# class Nm_cnrt(enum.Enum):
#     TUN = "+216"
#     MAR = "+212"
# User Model
class User(AbstractUser):
#     choice_num = ((Nm_cnrt.TUN.value, "+216"),
#                   (Nm_cnrt.MAR.value, "+212"))
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # phone_nm = models.IntegerField("phone_nm", choices=choice_num, default=Nm_cnrt.TUN.value , blank=True) # check length number !!!
    # country_nm = models.IntegerField(validators=[check_country_nm]) checking !!!
    def __str__(self):
        return self.username


# Run create_auth_token after user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Run password_reset_token_created after receiving reset_password_token_created signal
@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):

    email_plaintext_message = "http://localhost:8000/reset-password/{}".format(
        reset_password_token.key
    )

    send_mail(
        # title:
        "Password Reset for {title}".format(title="bibliothèque en ligne "),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],
    )





