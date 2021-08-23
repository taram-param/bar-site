from django.urls import path

from . import views

urlpatterns = [
    path("", views.CollectionsView.as_view(), name="index"),
    path("photo/", views.AllCollectionsView.as_view(), name="all_collections"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("<slug:slug>/", views.CollectionDetailView.as_view(), name="collection_detail"),
    path("video/<slug:slug>/", views.VideoDetailView.as_view(), name="video_detail"),
    path("place/<slug:slug>/", views.PlaceDetailView.as_view(), name="place_detail"),
]