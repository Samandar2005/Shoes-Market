from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from toys.models import Shoes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import ShoesSerializer


def test_api_view(request):
    first_shoes = Shoes.objects.first()
    f_b = {
        'name': first_shoes.name,
        'brand': first_shoes.brand.name,
        'company': first_shoes.company.title,
        'color': first_shoes.color,
        'сompound': first_shoes.сompound.name,
        'material': [item.name for item in first_shoes.material.all()],
        'date': first_shoes.date
    }
    return JsonResponse(f_b)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def shoes_api_view(request, pk=0):

    if request.method == 'GET':
        if pk == 0:
            return Response(data=ShoesSerializer(instance=Shoes.objects.all(), many=True).data, status=200)
        else:
            the_shoes = get_object_or_404(Shoes, pk=pk)
            return Response(data=ShoesSerializer(instance=the_shoes).data, status=200)

    elif request.method == "POST":
        sb = ShoesSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_shoes = get_object_or_404(Shoes, pk=pk)
        sb = ShoesSerializer(data=request.data, instance=the_shoes)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_shoes = get_object_or_404(Shoes, pk=pk)
        the_shoes.delete()
        return Response('Deleted', status=200)


def brand_api_view(request, pk=0):
    pass


class ShoesListAPIView(ListAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


class ShoesCreateAPIView(CreateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


class ShoesUpdateAPIView(UpdateAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer


class ShoesDestroyAPIView(DestroyAPIView):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
