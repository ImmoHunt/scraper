from django.shortcuts import render
#from rest_framework import viewset
#from .serializers import TodoSerializer
#from .models import TodoIt

#class TodoView(viewsets.ModelViewSet):
#	serializer_class = TodoSerializer
#	queryset = TodoIt.objects.all()

def index(request):
    return render(request, 'frontend/index.html')
