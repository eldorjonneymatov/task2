from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.company.models import Company, Review

from .permissions import IsReviewOwnerOrReadOnly
from .serializers import (CompanyProductSerializer,
                          CompanyReviewsStatsSerializer, CompanySerializer,
                          ReviewSerializer)


class CompanyDetailView(RetrieveAPIView):
    model_class = Company
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyProductsView(RetrieveAPIView):
    model_class = Company
    serializer_class = CompanyProductSerializer
    queryset = Company.objects.all()


class CompanyReviewStatsView(RetrieveAPIView):
    model_class = Company
    serializer_class = CompanyReviewsStatsSerializer
    queryset = Company.objects.all()


class CompanyReviewsListView(APIView):
    def get(self, request, *args, **kwargs):
        reviews = Review.objects.filter(company_id=self.kwargs["pk"])
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class CompanyReviewCreateView(CreateAPIView):
    model_class = Review
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        company = self.kwargs["company_pk"]
        serializer.save(company_id=company, profile=self.request.user.profile)
        return super().perform_create(serializer)


class CompanyReviewDeleteView(DestroyAPIView):
    model_class = Review
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated, IsReviewOwnerOrReadOnly]
