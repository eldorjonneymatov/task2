from django.db.models.aggregates import Sum
from rest_framework import serializers

from apps.company.models import Company, Product, Review


class CompanySerializer(serializers.ModelSerializer):
    review_info = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ("id", "name", "review_info")

    def get_review_info(self, obj):
        all_reviews = obj.reviews
        count = all_reviews.count()
        if count == 0:
            average = 0
        else:
            average = all_reviews.aggregate(rating_sum=Sum("rating"))["rating_sum"] / count
        return {"count": count, "average": average}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "discount")


class CompanyProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ("products",)


class CompanyReviewsStatsSerializer(serializers.ModelSerializer):
    rating_info = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ("rating_info",)

    def get_rating_info(self, obj):
        all_reviews = obj.reviews
        data = {}
        for i in range(1, 6):
            data[i] = all_reviews.filter(rating=i).count()
        return data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "rating", "comment", "company", "profile")
