from django.urls import include, path
from .views import *


urlpatterns = [
    path('test-api-view/', test_api_view),
    path('shoes-api-view/', ShoesListAPIView.as_view()),
    path('shoes-api-view/create', ShoesCreateAPIView.as_view()),
    path('shoes-api-view/update/<int:pk>', ShoesUpdateAPIView.as_view()),
    path('shoes-api-view/delete/<int:pk>', ShoesDestroyAPIView.as_view()),

    path('shoes-api-view/<int:pk>/', shoes_api_view),


    path('auth/', include('rest_framework.urls')),
]
