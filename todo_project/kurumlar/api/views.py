from urllib import response
from django.db.models.query import QuerySet
from rest_framework import pagination, serializers
from rest_framework.generics import GenericAPIView,get_object_or_404
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import generics
from kurumlar.api.Serializers import UserCreateSerializer,KurulusSerializer
from kurumlar.models import Kitaplar,Yorum,Kuruluslar
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from kurumlar.api.permissions import IsAdminUserOrReadOnly,IsYorumSahibiOrReadOnly
from kurumlar.api.pagination import SmallPagination,LargePagination
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions,views
from rest_framework.filters import SearchFilter,OrderingFilter



class KuruluslarListCreateAPIView(generics.ListCreateAPIView):
    queryset=Kuruluslar.objects.all()
    serializer_class=KurulusSerializer
    filter_backends=[SearchFilter]
    search_fields=['tür','ülke',"calisansayisi"]
    permission_classes = [IsAuthenticated]
    authentication_classes=[SessionAuthentication]

    
    
class KuruluslarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Kuruluslar.objects.all()
    serializer_class=KurulusSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[SessionAuthentication]




class RegisterUser(views.APIView):

    def post(self,request):
        serializers=UserCreateSerializer(request.data)

        if serializers.is_valid():
            serializers.save()
            return response(serializers.data)
        return response(serializers._errors)