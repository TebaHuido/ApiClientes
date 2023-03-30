from django.shortcuts import render
from .models import User, Profile , Permission
from rest_framework import viewsets,filters
from .serializers import UserSerializer
# Create your views here.reate/
def create(request):
    x=User(uname='shina',password='nada',mail='mail@mail.com',rut='12314123')
    x.save()
    return render(request, 'create.html')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #Sistema de filtros
    filter_backends = [filters.SearchFilter]
    search_fields = ['uname']
