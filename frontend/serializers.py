from rest_framework import serializers
from .models import TodoIt

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
	model = TodoIt
	fields = ('id', 'title', 'description', 'completed')
