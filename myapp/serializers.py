from rest_framework import serializers
from .models import *
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
    publisher = PublisherSerializer()
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'isbn', 'publisher']

class ContributionSerializer(serializers.ModelSerializer):
    book = BookSerializers()
    class Meta:
        model = BookContributor
        fields = ['book','role']


class ContributorSerializer(serializers.ModelSerializer):
    bookcontributor_set = ContributionSerializer(many=True)
    contrib_number = serializers.ReadOnlyField()
    class Meta:
        model = Contributor
        fields = ['first_names', 'last_names','email', 'bookcontributor_set','contrib_number']
