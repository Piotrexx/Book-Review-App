from rest_framework import serializers

class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField()
    website = serializers.URLField()
    email = serializers.EmailField()

class BookSerializers(serializers.Serializer):
    title = serializers.CharField()
    publication_date = serializers.CharField()
    isbn = serializers.CharField()
    publisher = PublisherSerializer()