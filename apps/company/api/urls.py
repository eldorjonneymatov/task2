from django.urls import path

from .views import (CompanyDetailView, CompanyProductsView,
                    CompanyReviewCreateView, CompanyReviewDeleteView,
                    CompanyReviewsListView, CompanyReviewStatsView)

urlpatterns = [
    path("<int:pk>/", CompanyDetailView.as_view(), name="detail"),
    path("<int:pk>/products/", CompanyProductsView.as_view(), name="products"),
    path("<int:pk>/stats/", CompanyReviewStatsView.as_view(), name="stats"),
    path("<int:pk>/reviews/", CompanyReviewsListView.as_view(), name="review_list"),
    path("<int:company_pk>/reviews/create/", CompanyReviewCreateView.as_view(), name="review_create"),
    path("<int:company_pk>/reviews/<int:pk>/delete/", CompanyReviewDeleteView.as_view(), name="review_delete"),
]
