from rest_framework.serializers import ModelSerializer
from main.models import Todo


class CreateToDoSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Todo