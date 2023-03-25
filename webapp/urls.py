from django.urls import path

from webapp.views.products import ProductDetail, ProductUpdateView, \
    ProductCreateView, ProductDeleteView
from webapp.views.reviews import ReviewCreateView
from webapp.views.base import IndexView, IndexRedirectView

urlpatterns =[
    path("", IndexView.as_view(), name='index'),
    path("product/", IndexRedirectView.as_view(), name='products_index_redirect'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/confirm_delete/', ProductDeleteView.as_view(), name='confirm_delete'),
    path('review/add/<int:pk>/', ReviewCreateView.as_view(), name='add_review')
]