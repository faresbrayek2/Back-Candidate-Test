from rest_framework import serializers

class LabelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class DocumentSerializer(serializers.Serializer):
    content = serializers.JSONField()

class AnnotationSerializer(serializers.Serializer):
    start = serializers.IntegerField()
    end = serializers.IntegerField()
    label = LabelSerializer()
    document = DocumentSerializer()
