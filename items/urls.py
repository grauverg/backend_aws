from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('item/', views.ItemListCreateAPIView.as_view()),

    # functions
    path('function/item/', views.item_list_create_api_view),
    path('function/item/<int:pk>/', views.item_retrieve_update_destroy_api_view),

    # my generic
    path('class/item/', views.ItemListCreateView.as_view()),
    path('class/item/<int:pk>', views.ItemRetrieveDestroyAPIView.as_view()),

    # viewsets
    # path('viewset/category/', views.CategoryViewSet.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('viewset/category/<int:pk>', views.CategoryViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    # )),
    path('viewset/', include(router.urls)),
]
