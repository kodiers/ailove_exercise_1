from rest_framework import serializers

from .models import Keys


class KeysSerializer(serializers.ModelSerializer):
    """
    Keys class serializer
    """
    class Meta:
        model = Keys
        fields = ('id', 'key', 'status')