from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', index),
    path('main/', index, name='main'),
    path('collection/', collection, name='collection'),
    path('contact/', contact, name="contact"),
    path('shoes/', shoes, name="shoes"),
    path('shoes_add/', shoes_add, name="shoes_add"),
    path('racing_boots/', racingboots, name="racing_boots"),
    path('shoes_base/', ShoesListViewMain.as_view(), name="shoes_base"),
    path('brand/', BrandListView.as_view(), name='brand'),
    path('brand/add', BrandCreateView.as_view(), name='brand-add'),
    path('brand/change/<int:pk>', BrandUpdateView.as_view(), name='brand-change'),
    path('brand/delete/<int:pk>', BrandDeleteView.as_view(), name='brand-delete'),
    path('company/', CompanyListView.as_view(), name='company'),
    path('company/add', CompanyCreateView.as_view(), name='company-add'),
    path('company/change/<int:pk>',
         CompanyUpdateView.as_view(), name='company-change'),
    path('company/delete/<int:pk>',
         CompanyDeleteView.as_view(), name='company-delete'),

    path('compound/', CompoundListView.as_view(), name='compound'),
    path('compound/add', CompoundCreateView.as_view(), name='compound-add'),
    path('compound/change/<int:pk>',
         CompoundUpdateView.as_view(), name='compound-change'),
    path('compound/delete/<int:pk>',
         CompoundDeleteView.as_view(), name='compound-delete'),

    path('material/', MaterialListView.as_view(), name='material'),
    path('material/add', MaterialCreateView.as_view(), name='material-add'),
    path('material/change/<int:pk>',
         MaterialUpdateView.as_view(), name='material-change'),
    path('material/delete/<int:pk>',
         MaterialDeleteView.as_view(), name='material-delete'),

    path('shoes_main/', cache_page(60*60)
         (ShoesListView.as_view()), name='shoes12'),
    path('shoes/add', ShoesCreateView.as_view(), name='shoes-add'),
    path('shoes/change/<int:pk>',
         ShoesUpdateView.as_view(), name='shoes-change'),
    path('shoes/delete/<int:pk>',
         ShoesDeleteView.as_view(), name='shoes-delete'),
    path('register/', user_register_view, name='register'),
    path('login/', user_login_view, name='login'),
    path('shoes-order/<int:pk>', user_login_view, name='shoes-order'),
    path('profile/', profile, name='user-profile'),
    path('order/', order, name='order'),
]
