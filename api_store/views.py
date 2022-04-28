from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Product, Store, Category
from .serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def product_list(request, spk, cpk):

    try:
        store = Store.objects.get(pk=spk)
    except Store.DoesNotExist:
        return HttpResponse(status=404)
    try:
        category = Category.objects.get(pk=cpk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        category = Category.objects.filter(store__id=spk).get(id=cpk)
        product = category.product_set.all()
        serializer = ProductSerializer(product, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def product_detail(request, spk, cpk, pk):
 
    try:
        store = Store.objects.get(pk=spk)
    except Store.DoesNotExist:
        return HttpResponse(status=404)
    try:
        category = Category.objects.get(pk=cpk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)
    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE': 
        product.delete()
        return HttpResponse(status=204)

    
@csrf_exempt
def product_chages(request,pk):
    try:
        product = Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        # serializer = ProductSerializer.shw_udt_cnt(product)
        # product['id']
        # return JsonResponse(serializer.data)
        serializer=dict()
        serializer=product.__getattribute__('update_counter')
        # return('{"update_counter":'+serializer+'}')
        return(serializer)