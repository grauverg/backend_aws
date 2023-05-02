from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, views, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer
from .my_generic import GenericListCreateView, GenericRetrieveDeleteUpdateView


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    """
    Category create and list view.

    :param Limit: int
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@api_view(http_method_names=['GET', 'POST'])
def item_list_create_api_view(request):
    # print(request.query_params)
    # print(request.data)
    # data = [
    #     {
    #         'name': 'Codify',
    #         'address': "7 md"
    #     }
    # ]
    if request.method == 'GET':
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def item_retrieve_update_destroy_api_view(request, pk):
    item = get_object_or_404(Item, pk=pk)

    # try:
    #     item = Item.objects.get(pk=pk)
    # except Item.DoesNotExist:
    #     return Response({'detail': 'no object'}, status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(instance=item)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ItemSerializer(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        item.delete()
        return Response(status=204)


class ItemListCreateView(GenericListCreateView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemRetrieveDestroyAPIView(GenericRetrieveDeleteUpdateView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

