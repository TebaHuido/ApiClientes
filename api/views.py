from django.shortcuts import render
from .models import User, Profile , Permission
from rest_framework import viewsets,filters
from .serializers import UserSerializer
# Create your views here.reate/
def create(request):
    x=User(uname='shina',password='nada',mail='mail@mail.com',rut='12314123')
    x.save()
    return render(request, 'create.html')
def home(request):
    user= User.objects.all()
    return render(request, 'home.html',{'users':user})
def post(request):
    return render(request, 'posts.html')
def descargar(request):
    return render(request, 'descargar.html')
def subir(request):
    return render(request, 'subir.html')
def acerca(request):
    return render(request, 'acerca.html')
def recursos(request):
    return render(request, 'recursos.html')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #Sistema de filtros
    filter_backends = [filters.SearchFilter]
    search_fields = ['uname']
