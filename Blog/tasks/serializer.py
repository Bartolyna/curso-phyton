
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('id','title', 'description', 'done') Esta es un forma de convertir tipos de datos de phyton a json
        fields = '__all__'