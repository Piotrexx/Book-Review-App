from rest_framework import serializers
from .models import Book, Publisher
# class PublisherSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     website = serializers.URLField()
#     email = serializers.EmailField()

# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField()
#     publication_date = serializers.CharField()
#     isbn = serializers.CharField()
#     publisher = PublisherSerializer()




# Model Serielizing
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'website', 'email']

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'isbn', 'publisher']