import logging
import json
import requests
from datetime import timezone
import datetime
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from rest_framework.decorators import api_view
from .serializers import *
from .models import ProductsTable
logger = logging.getLogger('file')

@api_view(['GET'])
def dishes(request):
    try:
     menu_dishes_objs = ProductsTable.objects.all()
     menu_list = []
     menu_dict = {}
    except Exception as exception:
        logger.error("Exception",exception)
    for menu_dishes_obj in menu_dishes_objs:
        menu_dict = {}
        menu_dict['name'] = menu_dishes_obj.name
        menu_dict['price'] = menu_dishes_obj.price
        print(menu_list)
        menu_list.append(menu_dict)
    return JsonResponse({'menu_list': menu_list})
