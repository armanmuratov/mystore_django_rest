from unicodedata import name
from rest_framework import serializers
from .models import Category
from .models import Product
from .models import Store

class StoreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    store = serializers.CharField(max_length=50)

class ProductSerializer(serializers.ModelSerializer):        
    category_id = serializers.HiddenField(default = 1)
    id = serializers.HiddenField(default = 1)
    name = serializers.CharField(max_length=50)
    update_counter = serializers.HiddenField(default = 1)

    class Meta:
        model = Product
        fields = ['category_id','id','name','update_counter']

    def create(self, validated_data,cpk):
        product = Product.objects.create(
            category_id=validated_data.get('category_id'),
            name=validated_data.get('name')
        )        
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.update_counter += 1
        instance.save()
        return instance

    def shw_udt_cnt(self):
        field=self['update_counter']
        return('{"update_counter":'+field+'}')