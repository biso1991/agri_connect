from rest_framework import serializers
from .models import Blogmodel

class BlogSerializer(serializers.ModelSerializer):
   class Meta:
        model = Blogmodel
        fields = '__all__'
    