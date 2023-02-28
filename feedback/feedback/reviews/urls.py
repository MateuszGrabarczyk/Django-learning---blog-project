from . import views
from django.urls import path

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/favourite", views.AddFavouriteView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view()),
    
]