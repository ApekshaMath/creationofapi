from rest_framework import serializers
from .models import Pro

class ProSerializers(serializers.ModelSerializers):
    class Meta:
        model = Pro
        fields = ('full_name','email','phone','country')

