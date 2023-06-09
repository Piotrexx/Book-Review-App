from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated, PermissionDenied

from .models import *
from .utils import average_rating








# # class PublisherSerializer(serializers.Serializer):
# #     name = serializers.CharField()
# #     website = serializers.URLField()
# #     email = serializers.EmailField()

# # class BookSerializers(serializers.Serializer):
# #     title = serializers.CharField()
# #     publication_date = serializers.CharField()
# #     isbn = serializers.CharField()
# #     publisher = PublisherSerializer()
    




# # Model Serielizing
class PublisherSerializer(serializers.ModelSerializer):
    class Meta: #  in Meta class we describe what model are we using and what fields from that model, we have to use Meta class when working with ModelSerialzers
        model = Publisher
        fields = ['name', 'website', 'email']

class BookSerializers(serializers.ModelSerializer):
    publisher = PublisherSerializer() # we need to add publisher variable to declare the publisher field from Book model. Plus we want to display Book and it's publisher. This operation is posibble to the ForeignKey in models.py
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'isbn', 'publisher']

class ContributionSerializer(serializers.ModelSerializer):
    book = BookSerializers() # The same goes to this
    class Meta:
        model = BookContributor
        fields = ['book','role']


class ContributorSerializer(serializers.ModelSerializer):
    bookcontributor_set = ContributionSerializer(many=True) # many=True that means that queryset have many sets of items 
    contrib_number = serializers.ReadOnlyField()
    class Meta:
        model = Contributor
        fields = ['first_names', 'last_names','email', 'bookcontributor_set','contrib_number']




class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ['name', 'website', 'email']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email']


class ReviewSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    book = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['pk', 'content', 'date_created', 'date_edited', 'rating', 'creator', 'book', 'book_id']

    def create(self, validated_data):
        request = self.context["request"]
        creator = request.user
        if not creator.is_authenticated:
            raise NotAuthenticated('Authentication required.')
        book = Book.objects.get(pk=request.data['book_id'])
        return Review.objects.create(content=validated_data['content'], book=book, creator=creator,
                                     rating=validated_data['rating'])

    def update(self, instance, validated_data):
        request = self.context['request']
        creator = request.user
        if not creator.is_authenticated or instance.creator_id != creator.pk:
            raise PermissionDenied('Permission denied, you are not the creator of this review')
        instance.content = validated_data['content']
        instance.rating = validated_data['rating']
        instance.date_edited = timezone.now()
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()
    rating = serializers.SerializerMethodField('book_rating')
    reviews = serializers.SerializerMethodField('book_reviews')

    def book_rating(self, book):
        reviews = book.review_set.all()
        if reviews:
            return average_rating([review.rating for review in reviews])
        else:
            None

    def book_reviews(self, book):
        reviews = book.review_set.all()
        if reviews:
            return ReviewSerializer(reviews, many=True).data
        else:
            None

    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'isbn', 'publisher', 'rating', 'reviews']