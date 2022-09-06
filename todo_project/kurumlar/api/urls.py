from django.urls import path,include
from kurumlar.api import views

urlpatterns = [

    path('register/',views.RegisterUser.as_view(), name='register'),
    path('kuruluslar/',views.KuruluslarListCreateAPIView.as_view(), name='kurulus-listesi'),
    path('kuruluslar/<int:pk>',views.KuruluslarDetailAPIView.as_view(), name='kurulus-bilgileri'),

]
