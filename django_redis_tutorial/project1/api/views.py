import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response



# connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


@api_view(['GET', 'POST'])
def manage_items(request, *args, **kwargs):
    if request.method == 'GET':
        items = {}
        count = 0
        for key in redis_instance.keys("*"):
            if redis_instance.type(key).decode() == "string":
                items[key.decode("utf-8")] = redis_instance.get(key)
            if redis_instance.type(key).decode() == "list":
                items[key.decode("utf-8")] = [ val.decode() for val in redis_instance.lrange(key, 0, -1) ]
            
            count += 1
        response = {
            'count': count,
            'msg': f"Found {count} items.",
            'items': items,
            "req_get": str(request.GET),
            "req_get": str(request.GET),
            "kwargs": str(kwargs)
        }
        return Response(response, status=200)

    elif request.method == 'POST':
        item = json.loads(request.body)
        key = list(item.keys())[0]
        value = item[key]
        redis_instance.set(key, value)
        response = {
            'msg': f"{key} successfully set to {value}",
            "req": str(request),
            "kwargs": str(kwargs)
        }
        return Response(response, 201)


@api_view(['GET', 'PUT', 'DELETE'])
def manage_item(request, *args, **kwargs):
    if request.method == 'GET':
        if kwargs['key']:
            value = redis_instance.get(kwargs['key'])
            if value:
                response = {
                    'key': kwargs['key'],
                    'value': value,
                    'msg': 'success',
                    "req": str(request),
                    "kwargs": str(kwargs)
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found',
                    "req": str(request),
                    "kwargs": str(kwargs)
                }
                return Response(response, status=404)

    elif request.method == 'PUT':
        if kwargs['key']:
            request_data = json.loads(request.body)
            new_value = request_data['new_value']
            value = redis_instance.get(kwargs['key'])
            if value:
                redis_instance.set(kwargs['key'], new_value)
                response = {
                    'key': kwargs['key'],
                    'value': value,
                    'msg': f"Successfully updated {kwargs['key']}",
                    "req": str(request),
                    "kwargs": str(kwargs)
                }
                return Response(response, status=200)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found',
                    "req": str(request),
                    "kwargs": str(kwargs)
                }
                return Response(response, status=404)

    elif request.method == 'DELETE':
        if kwargs['key']:
            result = redis_instance.delete(kwargs['key'])
            if result == 1:
                response = {
                    'msg': f"{kwargs['key']} successfully deleted"
                }
                return Response(response, status=404)
            else:
                response = {
                    'key': kwargs['key'],
                    'value': None,
                    'msg': 'Not found'
                }
                return Response(response, status=404)
