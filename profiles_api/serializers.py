from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializer a name field to test out APIView"""
    name = serializers.CharField(max_length=10)
           