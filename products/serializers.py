from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import Product, Review
from django.db.models import Avg

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    average_rating = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'average_rating', 'reviews_count', 'image', 'owner']
        read_only_fields = ['owner']

    def get_average_rating(self, obj):
        result = obj.reviews.aggregate(Avg('rating'))
        if result['rating__avg'] is None:
            return 0.0
        return round(result['rating__avg'], 1)

    def get_reviews_count(self, obj):
        return obj.reviews.count()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        return user

class ReviewSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ['id', 'product', 'user', 'author_name', 'rating', 'text', 'created_at']
        read_only_fields = ['user']