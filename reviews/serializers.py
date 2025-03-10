from rest_framework import serializers
from .models import Movie, Review, Category

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)  

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'average_rating', 'category', 'image', 'reviews']

        
