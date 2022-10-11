from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from ApisUsers.models import Users
from ApisUsers.serializers import UsersSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST','DELETE'])
def User_lista(request):
    if request.method == 'GET':
        users = Users.objects.all()

        name=request.GET.get('name',None)
        if name is not None:
            users = users.filter(name__icontains=name)
        users_serializer=UsersSerializer(users,many=True)
        return JsonResponse(users_serializer.data, safe=False)
    
    elif request.method == 'POST':
        user_data=JSONParser().parse(request)
        users_serializer=UsersSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Users.objects.all().delete()
        return JsonResponse({'message':'{} usuario eliminado satisfactoriamente!'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE']) 
def User_detalle(request,pk):
    try:
        users = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return JsonResponse({'message':'usuario no existe!'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        users_serializer=UsersSerializer(users)
        return JsonResponse(users_serializer.data)
    
    elif request.method=='PUT':
        producto_data=JSONParser().parse(request)
        users_serializer=UsersSerializer(users,data=producto_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data)
    
    elif request.method=='DELETE':
        users.delete()
        return JSONParser({'message':'usuario borrado!'},status=status.HTTP_204_NO_CONTENT)